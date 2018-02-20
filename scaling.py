import cv2
import numpy as np
import math
from dingusImageLib import Interpolation

def scaleImage(img,fac_x=1,fac_y=1):
    newHeight,newWidth = fac_y * img.shape[0] , fac_x * img.shape[1]
    newImg = np.zeros((newHeight,newWidth,img.shape[2]),np.uint8)

    for y in range(newHeight):
        for x in range(newWidth):
            newImg[y][x] = Interpolation.bilinear(img,float(x/fac_x),float(y/fac_y))
    
    return newImg
            
        
    

# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
textPos                = (30,220)
fontScale              = 0.50
fontColor              = (255,240,240)
lineType               = 2     



img = cv2.imread('lena.png')
cv2.putText(img,'Original',textPos,font,fontScale,fontColor,lineType)


for fac_x,fac_y in zip([1,2],[2,1]):
    newImg = scaleImage(img,fac_x,fac_y)
    cv2.imshow("Scaling fac : "+str(fac_x) + ","+ str(fac_y),newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

