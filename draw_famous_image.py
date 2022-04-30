import matplotlib.pyplot as plt
from scipy import misc


image = misc.ascent()
plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(image)
plt.show()
