import cv2
import numpy as np


img = cv2.imread('l.png',)
# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
pos                    = (100,100)
fontScale              = 0.50
fontColor              = (255,255,255)
lineType               = 1    

cv2.putText(img,'OpenCV',pos, font,fontScale,fontColor,lineType)
cv2.imshow('SAMPLING',img)

cv2.waitKey(0)
cv2.destroyAllWindows()