
def _compute_fans(shape):
    """Computes the number of input and output units for a weight shape.
    Arguments:
      shape: Integer shape tuple or TF tensor shape.
    Returns:
      A tuple of scalars (fan_in, fan_out).
    """
    if len(shape) < 1:  # Just to avoid errors for constants.
        fan_in = fan_out = 1
    elif len(shape) == 1:
        fan_in = fan_out = shape[0]
    elif len(shape) == 2:
        fan_in = shape[0]
        fan_out = shape[1]
    else:
        # Assuming convolution kernels (2D, 3D, or more).
        # kernel shape: (..., input_depth, depth)
        receptive_field_size = 1.
        for dim in shape[:-2]:
            receptive_field_size *= dim
        fan_in = shape[-2] * receptive_field_size
        fan_out = shape[-1] * receptive_field_size
    return fan_in, fan_out

# for conv layer
W = 4
H = 4
C = 1
F = 12
fan_in, fan_out = _compute_fans([H, W, C, F])
print(fan_in)
print(fan_out)