import matplotlib.pyplot as plt
import numpy as np
from utils import *

nrows = 4
NDATA = 5000

# Curves
f, axs = plt.subplots(nrows,nrows)
f.suptitle("Curves")
for i in range(nrows):
    for j in range(nrows):
        rand = np.random.randint(NDATA)
        data = np.load("./Train/curves/curve_"+str(rand).zfill(4)+".npy")
        axs[i,j].imshow(data, interpolation='nearest', aspect='auto')
        axs[i,j].axis('off')

# Lines
f, axs = plt.subplots(nrows,nrows)
f.suptitle("Lines")
for i in range(nrows):
    for j in range(nrows):
        rand = np.random.randint(NDATA)
        data = np.load("./Train/lines/line_"+str(rand).zfill(4)+".npy")
        axs[i,j].imshow(data, interpolation='nearest', aspect='auto')
        axs[i,j].axis('off')

plt.show()
