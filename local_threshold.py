from skimage.filters import threshold_local
#from scipy.misc import imread, imsave, imresize
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('histnormresult_big_trans.jpg', 0)

new_img = img > threshold_local(img, 15)

plt.imshow(new_img, cmap = plt.cm.gray)
plt.axis('off')
plt.show()
