# Misc
Miscellaneous functions and codes for Python, OpenCV, Tensorflow, and so on

#### Utils
* [canny_visualizer.py](canny_visualizer.py) Opens an image and applies Canny filter to it. You can play with the thresholds in the trackbars.
* [hsv_map.py](hsv_map.py) Opens an image and you can play with the HSV values in the trackbars.
* [hough_line_mapper.py](hough_line_mapper.py) Opens an image and you can play with Hough line detection parameters in the trackbars
  
#### OpenCV
* [convert_to_bw.py](convert_to_bw.py) Opens an image, applies binary thresholding, and saves it in red.
* [threshold_sample.py](threshold_sample.py) Shows the effect of different thresholding methods in OpenCV.
* [draw_famous_image.py](draw_famous_image.py) Draws a few famous pictures for image processing
* [k_means.py](k_means.py) Takes an image and using K-means method, clusters its color (using LAB color-space).
* [hue_based_histo.py](hue_based_histo.py) Masks the image with different Hue ranges and generates the histogram of brightness & saturation for the resulting image.
* [imutils.py](imutils.py) A small library with functions to rotate, translate, and resize images, and display multiple images in one plot.
* [test_hist_equalization.py](test_hist_equalization.py) Histogram matching 

#### I/O Operations
* [mouse_move.py](mouse_move.py) Moves the mouse cursor (Windows).
* [test_midi.py](test_midi.py) Communicate with MIDI device.
  
#### File Operations
* [dxf_writer.py](dxf_writer.py) Creates a dxf file and adds a line, polyline, and a layer to the file.
* [ms_word.py](ms_word.py) Creates a .docx file and adds text, headings, and a picture to the file.
* [ssh_utils.py](ssh_utils.py) A library for ssh & sftp operations.
* [yaml_writer.py](yaml_writer.py) Read and write Yaml files.
* [read_video.py](read_video.py) Reads and plays an MP4 video file until Q is pressed.

#### Graph Annotation in pyPlot
* [test_annotate.py](test_annotate.py) Tests plot annotation v1.
* [test_annotate2.py](test_annotate2.py) Tests plot annotation v2.
* [test_annotate3.py](test_annotate3.py) Tests plot annotation v3.

#### Python & Numpy
* [test_mult.py](test_mult.py) Compare np.dot, np.matmul, and np.multiply

#### Convolution
* [test_conv_tensorflow.py](test_conv_tensorflow.py) How to apply convolution to an image with custom filter using tensorflow
* [test_conv2d.py](test_conv2d.py) How to apply convolution to an image with custom filter using tensorflow
* [test_conv_loop.py](test_conv_loop.py) Perform convoltion element-by-element in a loop
* [test_conv_filter.py](test_conv_filter.py) Applies convolution using cv2.filter and a filter implementation function

#### Tensorflow
* [test_gradient.py](test_gradient.py) Use tf.GradientTape to calculate the derivative of a function
* [test_repeat.py](test_repeat.py) tf.repeat function
* [test_fan_in_fan_out.py](test_fan_in_fan_out.py) Check tensorflow fan_in & fan_out function
* [test_map_fn.py](test_map_fn.py) tf.map_fn ***
* [test_map_fn2.py](test_map_fn2.py) tf.map_fn ***
* [test_depthwise_conv2d.py](test_depthwise_conv2d.py) tf.depthwise_conv2d ***

#### Multiprocessing
* [multiprocess_Process.py](multiprocess_Process.py) multiprocessing.Process
* [multiprocess_pool.py](multiprocess_pool.py) multiprocessing.pool

