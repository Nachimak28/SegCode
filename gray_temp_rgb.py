import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('thermal.jpg', 0)
plt.imshow(img, cmap = 'gray')
plt.show()
final = cv2.applyColorMap(img, cv2.COLORMAP_JET)

cv2.imshow('Image', final)
cv2.imwrite('thermal_img.jpg', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
