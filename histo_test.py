import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import cv2




def plot_histo(image):
    img = cv2.imread(image)
    vals = img.mean(axis=2).flatten()
    counts, bins = np.histogram(vals, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()
    plt.clf()
    #plt.savefig('test.JPEG')


def plot_histo_clr(image):
    im = cv2.imread(image)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([im], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()
    plt.clf()
    #plt.savefig('testclr.JPEG')

#img_one_ch = 'app/static/imagenet_subset/n01494475_hammerhead.JPEG'
#plot_histo(img_one_ch)

#img_clr = 'app/static/imagenet_subset/n01494475_hammerhead.JPEG'
#plot_histo_clr(img_clr)
