import numpy as np
np.set_printoptions(precision=2, suppress=True)
import cv2
import matplotlib.pyplot as plt


from LogGabor import LogGabor
ns = 500
img = cv2.imread('histnormresult_big1.png', 0)
img = cv2.resize(img, (ns, ns))
#parameterfile = 'https://raw.githubusercontent.com/bicv/LogGabor/master/default_param.py'
parameterfile = {
# Image
# 'N_image' : None, #use all images in the folder
'N_image' : 100, #use 100 images in the folder
# 'N_image' : 10, #use 4 images in the folder
'seed' : None, # a seed for the Random Number Generator (RNG) for picking images in databases, set to None xor set to a given number to freeze the RNG
'N_X' : ns, # size of images
'N_Y' : ns, # size of images
# 'N_X' : 64, # size of images
# 'N_Y' : 64, # size of images
'noise' : 0.1, # level of noise when we use some
'do_mask'  : True, # self.pe.do_mask
'mask_exponent': 3., #sharpness of the mask
# whitening parameters:
'do_whitening'  : True, # = self.pe.do_whitening
'white_name_database' : 'kodakdb',
'white_n_learning' : 0,
'white_N' : .07,
'white_N_0' : .0, # olshausen = 0.
'white_f_0' : .4, # olshausen = 0.2
'white_alpha' : 1.4,
'white_steepness' : 4.,
'white_recompute' : False,
# Log-Gabor
#'base_levels' : 2.,
'base_levels' : 1.618,
'n_theta' : 30, # number of (unoriented) angles between 0. radians (included) and np.pi radians (excluded)
'B_sf' : .4, # 1.5 in Geisler
'B_theta' : 3.14159/18.,
# PATHS
'use_cache' : True,
'figpath': 'results',
'edgefigpath': 'results/edges',
'matpath': 'cache_dir',
'edgematpath': 'cache_dir/edges',
'datapath': 'database',
'ext' : '.pdf',
'figsize': 14.,
'formats': ['pdf', 'png', 'jpg'],
'dpi': 450,
'verbose': 0,
}
#img = cv2.imread('trial_2.png', 0)


lg = LogGabor(parameterfile)
img = lg.whitening(img)*lg.mask

#global thresholding
med = []
for i in range(len(img)):
    for j in range(0,len(img[i]), 25):
        med.append(img[i][j])
        

#len(med)

S = np.median(med)

print(S)

#med

dev = []
for i in range(len(img)):
    for j in range(len(img[i])):
        dev.append(abs(img[i][j] - S))

#len(dev)

#dev

sd = np.median(dev)

print(sd)

alpha = 2  #change to higher values for different results
T = S - alpha * sd

print(T)

#plt.plot(np.arange(img[150].size), img[150], "ro")
n = 4
cp = img.copy()
for i in range(len(cp)):
    for j in range(len(cp[i])):
        if cp[i][j] <= n*T:
            cp[i][j] = 255

plt.title('Global Thresholding')
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img, cmap  = 'gray')
plt.subplot(1,2,2)
plt.title('Global Thresholding')
plt.imshow(cp, cmap = 'gray')
name = 'gt_alp_'+ str(alpha) + '_thm_' + str(n) + '.png'
#cv2.imwrite(name, cp)
plt.show()


#plt.imshow(img, cmap = 'gray')
#plt.show()