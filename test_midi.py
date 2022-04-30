import pygame.midi


def print_devices():
    for n in range(pygame.midi.get_count()):
        print(n, pygame.midi.get_device_info(n))


def readInput(input_device):
    while True:
        if input_device.poll():
            event = input_device.read(1)
            print(event)


if __name__ == '__main__':
    pygame.midi.init()
    print_devices()
    my_input = pygame.midi.Input(1)  # only in my case the id is 2
    readInput(my_input)
