import cv2 as cv


while True:
    img = cv.imread('input/modelTesting.jpg')

    cv.imshow('Original', img)
    cv.waitKey(0)