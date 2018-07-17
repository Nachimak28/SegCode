import cv2
import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

img = cv2.imread('histnormresult_big1.png', 0)

kernel = np.array([[0,0,-1,0,0],[0,0,-2,0,0],[-1,-2,0,2,1],[0,0,2,0,0],[0,0,1,0,0]])

import scipy.signal

edges = scipy.signal.convolve2d(img, kernel, 'valid')



plt.imshow(edges, cmap = 'gray')
plt.show()

uR = np.mean(edges)
sdR = np.std(edges)
alpha = 1.5
T = uR + alpha * sdR
print(T)


cp = edges.copy()

for i in range(len(cp)):
    for j in range(len(cp[i])):
        if cp[i][j] >= 2*T:
        	#test with T and 2*T
            cp[i][j] = 255
            
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img, cmap  = 'gray')
plt.subplot(1,2,2)
plt.title('Hybrid Gray scale model')
plt.imshow(cp, cmap = 'gray')
plt.show()

kernel1 = np.array([[4,3,2,1,-2,-5,-6,-5,-2,1,2,3,4],[4,3,2,1,-2,-5,-6,-5,-2,1,2,3,4],[4,3,2,1,-2,-5,-6,-5,-2,1,2,3,4],[4,3,2,1,-2,-5,-6,-5,-2,1,2,3,4],[4,3,2,1,-2,-5,-6,-5,-2,1,2,3,4]])
edges = scipy.signal.convolve2d(img, kernel1, 'valid')



plt.imshow(edges, cmap = 'gray')
plt.show()

uR = np.mean(edges)
sdR = np.std(edges)
alpha = 1.5
T = uR + alpha * sdR
print(T)


cp = edges.copy()

for i in range(len(cp)):
    for j in range(len(cp[i])):
        if cp[i][j] >= T:
        	#test with T and 2*T
            cp[i][j] = 255
            
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img, cmap  = 'gray')
plt.subplot(1,2,2)
plt.title('Hybrid Gray scale model')
plt.imshow(cp, cmap = 'gray')
plt.show()
