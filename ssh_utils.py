import os
import traceback
import paramiko  # pylint: disable=import-error
import stat
import time


class SSHClient():
    def __init__(self, host, port, username='', password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
            if self.username:
                self.ssh_client.connect(
                    self.host, self.port, self.username, self.password)
            else:
                self.ssh_client.connect(self.host, self.port)
        except Exception as e:
            print(f'ssh to "{host}" failed with "{e}"')

    def disconnect(self):
        self.ssh_client.close()

    def exec_command_list(self, cmd_list, wait_until_finish):
        result = True
        for cmd in cmd_list:
            result = result and self.exec_command(cmd, wait_until_finish)
        return result

    def exec_command(self, cmd, wait_until_finish):
        try:
            print(f'Executing "{cmd}"')
            _, stdout, stderr = self.ssh_client.exec_command(cmd)
            if wait_until_finish:
                while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
                    time.sleep(1)
            stdout_lines = stdout.readlines()
            stderr_lines = stderr.readlines()
            print('----------stdout----------')
            for line in stdout_lines:
                print(line.strip())
            print('--------------------------')
            print('----------stderr----------')
            for line in stderr_lines:
                print(line.strip())
            print('--------------------------')
            exit_status = stdout.channel.recv_exit_status()

            if exit_status == 0:
                print(f'Command "{cmd}" executed successfully!')
                return True
            else:
                print(
                    f'Command "{cmd}" failed. Error code: {str(exit_status)}')
                return False
        except Exception as e:  # pylint: disable=broad-except
            print(f'Error in command: "{cmd}", Error: {e}')
            traceback.print_exc()
            return False


class SFTPClient():
    def __init__(self, host, port, username='', password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        try:
            self.ssh_client = \
                SSHClient(self.host, self.port, self.username, self.password)
            self.sftp_client = self.ssh_client.ssh_client.open_sftp()
            print(f'Connected through sftp to "{host}".')
        except Exception as e:
            print(f'sftp to "{host}" failed with "{e}"')

    def disconnect(self):
        self.sftp_client.close()

    def _send_files_to_remote(self, local, remote, filter, recursive, keep_folder_structure, apply_except):
        # if apply_expct is False: only send filter files,
        # otherwise sends everything except filter files
        # if keep_folder_structure is false, it will copy all the
        # files to the root of remote folder
        self.create_folders_on_remote_non_recursive(local, remote)

        for item in os.listdir(local):
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)

            if os.path.isfile(local_item):
                if filter != '':
                    # apply the filter
                    if apply_except:
                        # copy everything but except_filter
                        if local_item.endswith(filter):
                            continue
                    else:  # use filter to filter out files
                        if not local_item.endswith(filter):
                            continue
                try:
                    self.sftp_client.put(local_item, remote_item)
                    print(
                        f'File "{local_item}" copied to remote "{remote_item}".')
                except Exception as e:
                    print(
                        f'Failed with sending file "{local_item}" to remote, error "{e}".')
            else:
                if recursive:
                    if keep_folder_structure:
                        self._send_files_to_remote(
                            local_item, remote_item, filter, recursive, keep_folder_structure, apply_except)
                    else:
                        self._send_files_to_remote(
                            local_item, remote, filter, recursive, keep_folder_structure, apply_except)

    def create_folder_on_remote(self, path, mode=511, ignore_existing=True):
        try:
            self.sftp_client.mkdir(path, mode)
            print(f'Folder "{path}" created on {self.host}.')
        except Exception as e:
            if ignore_existing:
                print(f'Folder "{path}" already exists on {self.host}.')
            else:
                print(
                    f'Creating folder "{path}" on {self.host} failed with "{e}".')

    def create_folders_on_remote_non_recursive(self, local, remote):
        # creates the local folder list inside remote (non-recursive)
        # remote folder must exist
        for item in os.listdir(local):
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)

            if os.path.isdir(local_item):
                self.create_folder_on_remote(remote_item)

    def create_folders_on_local_non_recursive(self, local, remote):
        # creates the remote folder list inside local (non-recursive)
        # local folder must exist
        for item in self.sftp_client.listdir(remote):
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)

            # find out if item on the remote is a file or is a folder
            fileattr = self.sftp_client.lstat(remote_item)
            # if stat.S_ISREG(fileattr.st_mode):
            #     print 'is File'
            if stat.S_ISDIR(fileattr.st_mode):
                if not os.path.exists(local_item):
                    os.mkdir(local_item)
                    print(f'Folder "{local_item}" created on local.')
                else:
                    print(f'Folder "{local_item}" already exists on local.')

    def receive_folder_from_remote(self, local, remote, recursive=True):
        self.create_folders_on_local_non_recursive(local, remote)

        for item in self.sftp_client.listdir(remote):
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)

            # find out if item on the remote is a file or is a folder
            fileattr = self.sftp_client.lstat(remote_item)
            if stat.S_ISREG(fileattr.st_mode):
                try:
                    self.sftp_client.get(remote_item, local_item)
                    print(f'File "{remote_item}" received from remote.')
                except Exception as e:
                    print(
                        f'Failed with receiving file "{remote_item}" from remote, error "{e}".')
            else:
                if recursive:
                    self.receive_folder_from_remote(
                        local_item, remote_item, True)

    def create_folder_structure_on_remote(self, local, remote):
        # creates the local folder structure inside remote (recursive)
        for item in os.listdir(local):
            local_dir = os.path.join(local, item)
            remote_dir = os.path.join(remote, item)

            if os.path.isdir(local_dir):
                self.create_folder_on_remote(remote_dir)
                self.create_folder_structure_on_remote(local_dir, remote_dir)

    def send_folder_to_remote(self, local, remote, recursive=True):
        self.create_folders_on_remote_non_recursive(local, remote)

        for item in os.listdir(local):
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)

            if os.path.isfile(local_item):
                try:
                    self.sftp_client.put(local_item, remote_item)
                    print(f'File "{local_item}" copied to remote.')
                except Exception as e:
                    print(
                        f'Failed with sending file "{local_item}" to remote, error "{e}".')
            else:
                if recursive:
                    self.send_folder_to_remote(local_item, remote_item, True)

    def receive_filelist_from_remote(self, local, remote, file_list):
        for item in file_list:
            local_item = os.path.join(local, item)
            remote_item = os.path.join(remote, item)
            try:
                self.sftp_client.get(remote_item, local_item)
                print(
                    f'File "{remote_item}" received from remote into {local_item}.')
            except Exception as e:
                print(
                    f'Failed with receiving file "{remote_item}" from remote, error "{e}".')

    def send_files_to_remote_with_filter(self, local, remote, filter='', recursive=True, keep_folder_structure=True):
        self._send_files_to_remote(
            local, remote, filter, recursive, keep_folder_structure, False)

    def send_files_to_remote_with_except_filter(self, local, remote, except_filter='', recursive=True, keep_folder_structure=True):
        self._send_files_to_remote(
            local, remote, except_filter, recursive, keep_folder_structure, True)


# if __name__ == "__main__":
#     try:
#         ssh_client = SSHClient('sarahlynn', 22)
#         ssh_client.exec_command('ls')
#     finally:
#         ssh_client.disconnect()

#     try:
#         sftp_client = SFTPClient('sarahlynn', 22)
#         sftp_client.create_folder_on_remote(r'C:\test_ssh')
#         sftp_client.create_folders_on_remote_non_recursive(\
#             r'C:\Users\sohra\test_framework',
#             r'C:\test_ssh')
#         sftp_client.create_folders_on_local_non_recursive(\
#             r'C:\Users\sohra\test_framework\tmp',
#             r'C:\test_ssh\f1')
#         sftp_client.receive_folder_from_remote(\
#             r'C:\Users\sohra\test_framework',
#             r'C:\test_ssh\f1',
#             True)
#         sftp_client.create_folder_structure_on_remote(r'C:\Users\sohra\test_framework',
#             r'C:\test_ssh\f1')
#         sftp_client.send_folder_to_remote(\
#             r'C:\Users\sohra\test_framework',
#             r'C:\test_ssh\f1',
#             True)
#         sftp_client.receive_filelist_from_remote(\
#             r'C:\Users\sohra\test_framework',
#             r'C:\test_ssh\f1',
#             ['dummy.bpcfg', 'run.py', 'tmp/xx.rtf'])
#         sftp_client.send_files_to_remote_with_except_filter(\
#             r'C:\Users\sohra\test_framework\tmp',
#             r'C:\test_ssh\f1',
#             except_filter='.rtf', recursive=False, keep_folder_structure=False)
#     finally:
#         sftp_client.disconnect()
