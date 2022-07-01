import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()

image = cv2.imread('input/modelTesting.jpg')

path = "EDSR_2x.pb"
sr.readModel(path)

sr.setModel("edsr", 2)

result = sr.upsample(image)

cv2.imwrite("output/modelTestingEDSR_2x.jpg", result)
