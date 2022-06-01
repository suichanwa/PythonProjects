import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()

image = cv2.imread('input/modelTesting.jpg')

path = "EDSR_x3.pb"
sr.readModel(path)

sr.setModel("edsr", 3)

result = sr.upsample(image)

cv2.imwrite("output/modelTestingEDSR_3x.jpg", result)