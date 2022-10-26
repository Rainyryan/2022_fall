import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('EKG_481-600/512.jpg')
origin_r = 375
origin_c = 120
height = 145
width = 305
outputs = []
for i in range(12):
    outputs.append(img[origin_r+height*(i//4):origin_r+height*(i//4+1), origin_c+width*(i%4):origin_c+width*(i%4+1), ::-1])

fig = plt.figure(figsize=(3,4))
for i in range(12):
    fig.add_subplot(3, 4, i+1)
    plt.imshow(outputs[i])
plt.show()
