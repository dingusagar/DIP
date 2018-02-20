import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


def getHistogram(img):
    hist = {x:0.0 for x in range(256)}
    normalisedHist = {}

    arr = img.flatten()
    for px in arr:
        hist[px] += 1

    for i in hist.keys():
        hist[i] = float(hist[i]/len(arr))

    return hist


def equalizeHistogram(img):
    hist = getHistogram(img)

    for x in range(1,256):
        hist[x] += hist[x-1]
    
    transform = {}
    for x in range(256):
        transform[x] = int(hist[x] * 255)
    
    return transform    

def modifyImage(img,transform):
    h,w = img.shape[0],img.shape[1]
    newImg = np.zeros((h,w),np.uint8)
    for i in range(h):
        for j in range(w):
            newImg[i][j] = transform[img[i][j]]
    return newImg
    
def histogramTransform(img1,img2):
    transform1 = equalizeHistogram(img1)
    transform2 = equalizeHistogram(img2)

    itransform2 = {} # inverse of transform2
    
    for key in transform2:
        if transform2[key] in itransform2:
            itransform2[transform2[key]] = int((itransform2[transform2[key]] + key)/2.0)
        else:
            itransform2[transform2[key]] = key
    
    finalTransform = {}
    for px in transform1.keys():
        finalTransform[px] = transform2[transform1[px]]
    
    newImg = modifyImage(img1,finalTransform)
    return newImg
        



def histogramEqu_main():      

    img = cv2.imread('lena.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    transform = equalizeHistogram(img)
    newImg = modifyImage(img,transform)

    cv2.imshow("Histogram Equalisation",np.hstack([img,newImg]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def histogramTransform_main():
    img1 = cv2.imread('lena.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img2 = cv2.imread('l.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)

    resultImg = histogramTransform(img1,img2)
    cv2.imshow("Before",img1)
    cv2.imshow("Using this to transform",img2)
    cv2.imshow("After",resultImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    # histogramEqu_main()
    histogramTransform_main()

    
