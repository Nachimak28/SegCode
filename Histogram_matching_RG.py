import cv2
import numpy as np
import scipy
import matplotlib.pyplot as plt
'''
#Taking input image
ip = cv2.imread('C://Users//nachiket//Desktop//RAYD8 tech//Reference material//retimg//13_left.jpeg')

#Resizing for faster reslts and small window size
rip = cv2.resize(ip, (300,300))

#split channels 
r,g = rip[:,:,2], rip[:,:,1]

#histograms of red and green channels
plt.subplot(2,2,1)
plt.hist(r.ravel(),256,[0,256], color = 'r') 
plt.title('Histgram of Red channel')
plt.subplot(2,2,2)
plt.hist(g.ravel(),256,[0,256], color = 'g') 
plt.title('Histgram of Green channel')
plt.subplot(2,2,3)
plt.title('Overlayed histograms of R and G channel')
plt.hist(r.ravel(),256,[0,256], color = 'r') 
plt.hist(g.ravel(),256,[0,256], color = 'g') 
plt.show()
#cv2.imshow('image',g)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
'''
#histogram comparison
from scipy.misc import imsave, imread
#import numpy as np

imsrc = imread("C://Users//nachiket//Desktop//RAYD8 tech//Reference material//retimg//Green_ch_big.jpeg")
imtint = imread("C://Users//nachiket//Desktop//RAYD8 tech//Reference material//retimg//Red_ch_big.jpeg")

nbr_bins=255
if len(imsrc.shape) < 3:
    imsrc = imsrc[:,:,np.newaxis]
    imtint = imtint[:,:,np.newaxis]

imres = imsrc.copy()
for d in range(imsrc.shape[2]):
    imhist,bins = np.histogram(imsrc[:,:,d].flatten(),nbr_bins,normed=True)
    tinthist,bins = np.histogram(imtint[:,:,d].flatten(),nbr_bins,normed=True)

    cdfsrc = imhist.cumsum() #cumulative distribution function
    cdfsrc = (255 * cdfsrc / cdfsrc[-1]).astype(np.uint8) #normalize

    cdftint = tinthist.cumsum() #cumulative distribution function
    cdftint = (255 * cdftint / cdftint[-1]).astype(np.uint8) #normalize


    im2 = np.interp(imsrc[:,:,d].flatten(),bins[:-1],cdfsrc)



    im3 = np.interp(im2,cdftint, bins[:-1])

    imres[:,:,d] = im3.reshape((imsrc.shape[0],imsrc.shape[1] ))

try:
    imsave("histnormresult_big.jpg", imres)
except:
    imsave("histnormresult_big.jpg", imres.reshape((imsrc.shape[0],imsrc.shape[1] )))
