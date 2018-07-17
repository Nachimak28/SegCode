import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('histnormresult_big.jpg',0)
print(img.shape)
#histo = np.histogram(img, bins = np.arange(0,256))
#plt.hist(img.ravel(),256,[0,256]) 
#plt.show()
#from skimage.feature import canny
#edges = canny(img/255.)
#from scipy import ndimage as ndi
#fill = ndi.binary_fill_holes(edges)


#from skimage import morphology

#cleaned = morphology.remove_small_objects(fill, 21)
#plt.imshow(cleaned, cmap=plt.cm.gray,interpolation='nearest')    # plot the edges_clipped
#plt.axis('off')
#plt.show()


from skimage.filters import sobel
elevation_map = sobel(img)

markers = np.zeros_like(img)
markers[img<120] = 1
markers[img>200] = 2
from skimage.morphology import watershed
segmentation = watershed(elevation_map, markers)

plt.imshow(segmentation, cmap = plt.cm.gray)
plt.axis('off')
plt.show()
