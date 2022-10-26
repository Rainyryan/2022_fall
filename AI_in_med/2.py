 import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os
import csv

def getHR_test(filepath):
    img = cv.imread(filepath)
    img1 = img[357+145*3:357+145*4, 120+3:120+305*4, 2]
    
    _, ekg = cv.threshold(img1, 140, 255, cv.THRESH_BINARY)
    ekg_plot = np.array([0 for i in range(ekg.shape[1])])
    for i in range(ekg.shape[1]):
        for j in range(ekg.shape[0])[::-1]:
            if (ekg[j,i] == 0):
                ekg_plot[i] = ekg.shape[0] - j
                break
    peaks, properties = find_peaks(ekg_plot,  distance=18, width=(0,6), prominence=1)
    print(properties['prominences'])
    peaks_parsed = []
    for i in range(peaks.shape[0]):
        if(properties['prominences'][i]>6):
            peaks_parsed.append(peaks[i])
    print("file:",filepath,"\nHeartrate:",len(peaks_parsed)*6)
    print("------------------------")
    cv.imshow("", ekg)
    plt.plot(np.arange(ekg.shape[1]), ekg_plot)
    plt.plot(peaks, ekg_plot[peaks], "rx")
    plt.plot(peaks_parsed, ekg_plot[peaks_parsed], "gx")
    plt.show()

def getHR(filepath):
    img = cv.imread(filepath)
    img1 = img[357+145*3:357+145*4, 120+3:120+305*4, 2]
    
    _, ekg = cv.threshold(img1, 140, 255, cv.THRESH_BINARY)
    ekg_plot = np.array([0 for i in range(ekg.shape[1])])
    for i in range(ekg.shape[1]):
        for j in range(ekg.shape[0])[::-1]:
            if (ekg[j,i] == 0):
                ekg_plot[i] = ekg.shape[0] - j
                break
    peaks, properties = find_peaks(ekg_plot,  distance=18, width=(0,6), prominence=1)
    peaks_parsed = []
    for i in range(peaks.shape[0]):
        if(properties['prominences'][i]>6):
            peaks_parsed.append(peaks[i])
    return len(peaks_parsed)*6

if __name__ == "__main__":
    path = 'EKG_481-600'
    # getHR_test('EKG_001-120/100.jpg')
    csv_file = open('heartbeat.csv', 'a', newline='')
    writer = csv.writer(csv_file)
    files = os.listdir(path)
    files.sort(key = lambda x:int(x[:-4])) #sort [number].jpg files by number
    # print(files)
    for file in files:
        try:
            hr = getHR(path+'/'+file)
            print(file, hr)
            writer.writerow([file, hr])
        except:
            print("an error occurred in", path+'/'+file)
    csv_file.close()

