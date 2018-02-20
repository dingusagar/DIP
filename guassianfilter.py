import cv2
import numpy as np
import math


def bilinear(img,x,y):
    base_x,base_y = math.floor(x),math.floor(y)
    dx,dy = x - base_x , y - base_y
    base_x,base_y = int(base_x),int(base_y)
    next_x,next_y = base_x + 1, base_y + 1

    if next_x > img.shape[1] -1 or next_y > img.shape[0] -1 or base_x > img.shape[1] -1 or base_y > img.shape[0] -1 :
        return 0*img.shape[2]
        

    value = (1-dx)*(1-dy)*img[base_y][base_x] + dx*dy*img[base_y+1][base_x+1] +  dx*(1-dy)*img[base_y][base_x+1] + dy*(1-dx)*img[base_y+1][base_x]
    return value

def getRotationMatrix(degree):
    c,s = np.cos(np.radians(degree)) , np.sin(np.radians(degree))
    return np.matrix([[c,-s],[s,c]])


def convolve(img,kernel):
    b,a = kernel.shape[0],kernel.shape[1]
    newImg = np.zeros(img.shape,np.uint8)

    for y in range(newImg.shape[0]):
        for x in range(newImg.shape[1]):
            value = 0
            for t in range(-1*(b-1)/2,(b-1)/2 + 1):
                for s in range(-1*(a-1)/2,(a-1)/2 + 1):
                    if x-s >=0 and x-s <img.shape[1] and y-t >=0 and y-t < img.shape[0]:
                        # print("--> "+ str(t + (b-1)/2) + " and " +str(s + (a-1)/2))
                        value += img[y-t][x-s] * kernel[t + (b-1)/2 , s + (a-1)/2]
                        
            newImg[y][x] = value
    
    return newImg

def generateGuassianKernel(size,sigma):
    kernel = np.zeros([size,size])
    sum = 0.0
    for y in range(size):
        for x in range(size):
            kernel[y,x] = np.exp(-1*((x+1)**2 + (y+1)**2)/(2*sigma*sigma))
            sum += kernel[y,x]
    for y in range(size):
        for x in range(size):
            kernel[y,x] /= sum
           
    return kernel    

        
    

img = cv2.imread('lena.png')
kernel = generateGuassianKernel(3,2.0)
cv2.imshow('convolution before and after ',np.hstack([img,convolve(img,kernel)]))
cv2.waitKey(0)
cv2.destroyAllWindows()

