import cv2 as cv
import sys

img = cv.imread('input/suisui.jpg')

if img is None:
    print('読み込みに失敗しました')
    sys.exit()

cv.imshow('suisui', img)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite('output/suisui.jpg', img)

