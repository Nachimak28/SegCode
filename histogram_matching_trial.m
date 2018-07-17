A = imread('C:\Users\nachiket\Desktop\RAYD8 tech\Reference material\Segmentation codebase\histnormresult.jpg')

[bw, thresh] = edge(A, "Canny")


imshow(bw)

