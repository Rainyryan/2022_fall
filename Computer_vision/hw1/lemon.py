#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import cv2 as cv
import numpy as np
from tomato import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

class My_Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda:self.loadimg(1))
        self.pushButton_2.clicked.connect(lambda:self.loadimg(2))
        self.pushButton_3.clicked.connect(lambda:self.separate())
        self.pushButton_4.clicked.connect(lambda:self.transform())
        self.pushButton_5.clicked.connect(lambda:self.detection())
        self.pushButton_6.clicked.connect(lambda:self._blend())
        self.pushButton_7.clicked.connect(lambda:self._gaussian())
        self.pushButton_8.clicked.connect(lambda:self._bilateral())
        self.pushButton_9.clicked.connect(lambda:self._median())
        
    def loadimg(self, num):
        filename, filetype = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), 'JPEG Files (*.jpg)')
        if filename:
            if num == 1:
                self.img1 = cv.imread(filename)
                self.label.setText(filename.split('/')[-1])
            if num == 2:
                self.img2 = cv.imread(filename)
                self.label_2.setText(filename.split('/')[-1])

    def separate(self):
        try:
            img = self.img1
            b,g,r = cv.split(img)
            zeros = np.zeros(img.shape[:2], dtype="uint8")
            self.separated_b = cv.merge([b, zeros, zeros])
            self.separated_g = cv.merge([zeros, g, zeros])
            self.separated_r = cv.merge([zeros, zeros, r])
            cv.imshow("b", self.separated_b)
            cv.imshow("g", self.separated_g)
            cv.imshow("r", self.separated_r)
        except:
            print("An error occurred")

    def transform(self):
        img = self.img1

        I1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow("I1", I1)

        split_img=np.array(cv.split(img),dtype='uint16')
        I2 = np.array((split_img[0]+split_img[1]+split_img[2])/3, dtype='uint8')
        cv.imshow("I2", I2)

    def detection(self):
        img = self.img1
        hsv_img = cv.cvtColor(img, cv.COLOR_RGB2HSV)

        low_g = np.array([40, 50, 20])
        high_g = np.array([80, 255, 255])
        g_mask = cv.inRange(hsv_img, low_g, high_g)

        img_g = cv.bitwise_and(img, img, mask=g_mask)
        cv.imshow("green", img_g)

        low_w = np.array([0, 0, 200])
        high_w = np.array([180, 20, 255])
        w_mask = cv.inRange(hsv_img, low_w, high_w)
        img_w = cv.bitwise_and(img, img, mask=w_mask)
        cv.imshow("white", img_w)

    def _blend(self):
        cv.namedWindow("Blend")
        cv.createTrackbar("Blend:", "Blend", 0, 255, self.blend)
        cv.setTrackbarPos("Blend:", "Blend", 127)
    
    def blend(self, val):
        weight2 = val/255
        img = cv.addWeighted(self.img1, 1-weight2, self.img2, weight2, 0)
        cv.imshow("Blend", img)

    def _gaussian(self):
        cv.namedWindow("gaussian_blur")
        cv.createTrackbar("magnitude:", "gaussian_blur", 0, 10, self.gaussian)
        self.gaussian(0)

    def gaussian(self, val):
        img = cv.GaussianBlur(self.img1, (2*val+1, 2*val+1), 1)
        cv.imshow("gaussian_blur", img)
    
    def _bilateral(self):
        cv.namedWindow("bilateral_filter")
        cv.createTrackbar("magnitude:", "bilateral_filter", 0, 10, self.bilateral)
        self.bilateral(0)

    def bilateral(self,val):
        img = cv.bilateralFilter(self.img1, 2*val+1, 90, 90)
        cv.imshow("bilateral_filter", img)
        
    def _median(self):
        cv.namedWindow("median_filter")
        cv.createTrackbar("magnitude:", "median_filter", 0, 10, self.median)
        self.median(0)

    def median(self, val):
        img = cv.medianBlur(self.img2, 2*val+1)
        cv.imshow("median_filter", img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = My_Window()
    window.show()
    sys.exit(app.exec_())