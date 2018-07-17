import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from skimage import exposure
img = cv2.imread('histnormresult_big.jpg',0)

print(img.shape)

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
#image_sharpen = scipy.signal.convolve2d(img, sharpen_kernel, 'valid')
kernel1 = np.array([[-1,0,-1], [0,0,0], [-1,0,1]])
#kernel2 = np.array([[0,1,0], [1,-4,1], [0,1,0]])
#kernel3 = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
edges = scipy.signal.convolve2d(img, kernel1, 'valid')

#edges_equalized = exposure.equalize_adapthist(edges/np.max(np.abs(edges)), clip_limit=0.03)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)
plt.imshow(edges, cmap=plt.cm.gray)    # plot the edges_clipped
plt.axis('off')
plt.show()
new = cv2.resize(edges, (500,500))
cv2.imwrite('trial_3.png', new)

