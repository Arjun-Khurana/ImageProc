import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

import sys
import os

imgs = []
files = []

def humanize(img):
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    cdf = hist.cumsum()
    cdf_humanized = cdf * float(hist.max())/cdf.max()

    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')

    img2 = cdf[img]
    return img2


for file in os.listdir(sys.argv[1]):
    if file.endswith('.tif'):
        files.append(file)
        img = cv.imread(os.path.join(sys.argv[1],file), 0)
        imgs.append(humanize(img))

if not os.path.exists('humanized'):
    os.mkdir('humanized')
for file, img in zip(files,imgs):
    cv.imwrite('humanized/{}'.format(file), img)



