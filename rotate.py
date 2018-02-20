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



def rotate(img,degree):
    newHeight,newWidth = img.shape[0] , img.shape[1]
    newImg = np.zeros((newHeight,newWidth,img.shape[2]),np.uint8)

    rotMatrix = getRotationMatrix(-1*degree) # interpolation is done by inverse function , so -1*degree

    for y in range(newHeight):
        for x in range(newWidth):
            point = np.matrix([[x - newWidth/2],[y - newHeight/2]])
            resultPoint = np.matmul(rotMatrix,point)
            newImg[y][x] = bilinear(img,resultPoint[0][0] + newWidth/2,resultPoint[1][0]  + newHeight/2)
    
    return newImg
            
        
    

img = cv2.imread('lena.png')
cv2.imshow('roated ',rotate(img,-5))
cv2.waitKey(0)
cv2.destroyAllWindows()

