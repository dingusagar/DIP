import cv2
import numpy as np


def sampleImg(img,factor):
    height = img.shape[0]
    width = img.shape[1]
    sampled = np.zeros((height,width,3), np.uint8)

    for i in range(0,height,height/factor):
        for j in range(0,width,width/factor):
            print ("Img[%d][%d]"%(i,j))
            sampled[i,j] = img[i,j]
    return sampled


def quantize(img,factor):
    height = img.shape[0]
    width = img.shape[1]
    quantized = np.zeros((height,width,3), np.uint8)

    quantum = 256/factor

    for channel in range(3):
        for i in range(height):
            for j in range(width):
                if img[i,j,channel] % quantum == 0:
                    level = np.ceil(img[i,j,channel] / quantum)
                    quantized[i,j,channel] = quantum * level

    return quantized

# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
textPos                = (50,200)
fontScale              = 0.50
fontColor              = (255,255,255)
lineType               = 2     


img = cv2.imread('l.png',)

sampledImgList = []
quantizedImgList = []
cv2.putText(img,'Original',textPos,font,fontScale,fontColor,lineType)

sampledImgList.append(img)
quantizedImgList.append(img)

for i in range(1,7):
    fac = pow(2,i)

    sampled = sampleImg(img,fac)
    cv2.putText(sampled,'Samping fac : '+str(fac),textPos,font,fontScale,fontColor,lineType)
    sampledImgList.append(sampled)




for i in range(1,9):
    fac = pow(2,i)

    quantized = quantize(img,fac)
    cv2.putText(quantized,'Quantization fac : '+str(fac),textPos,font,fontScale,fontColor,lineType)
    quantizedImgList.append(quantized)

cv2.imshow("Quantization",np.hstack(quantizedImgList))
cv2.imshow("SAmpling",np.hstack(sampledImgList))

cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.add(img,img)
# img = cv2.add(img,img)
# img = cv2.add(img,img)

# # blured = np.hstack([img,cv2.blur(img,(3,3)),cv2.blur(img,(5,5)),cv2.blur(img,(7,7))])
# # bluredG = np.hstack([img,cv2.GaussianBlur(img,(3,3),0),cv2.GaussianBlur(img,(5,5),0),cv2.GaussianBlur(img,(7,7),0)])

# # cv2.imshow("blur",blured)
# # cv2.imshow("Gblur",bluredG)

# cv2.waitKey(0)
# cv2.destroyAllWindows()