import numpy as np
import random
from scipy.stats import norm
import glob
import os

# DONOT CHANGE THESE VALUES
NSUB = 72
NBINS = 256

def poly(x, a=0.1, b=-3, c=50):
        return a*x**2 + b*x + c

def gen_rand_vars(a_range, b_range, c_range,
        width_range, snr_range, flip_sign = True):
    a = random.uniform(a_range[0], a_range[-1])
    b = random.uniform(b_range[0], b_range[-1])
    c = random.uniform(c_range[0], c_range[-1])

    if flip_sign:
        sign = random.randint(0,1)
        if sign:
            a *= -1
            b *= -1

    width = random.uniform(width_range[0], width_range[-1])
    snr = random.uniform(snr_range[0], snr_range[-1])
    return a,b,c,width,snr

def get_sub_rolls(nsub, a, b, c):
    x_poly = np.arange(0, nsub)
    return poly(x_poly, a, b, c)

def get_fake_data(nsub, nbins, width, snr):
    data = np.random.normal(size=(nsub,nbins))
    rv = norm(loc=nbins/2, scale=width)
    sig = rv.pdf(np.arange(0, nbins))
    sig /= sig.sum()
    sig = sig * snr / np.sqrt(nsub) * np.sqrt(width)
    return data + sig



def roll_matrix(data, roll):
    for i,row in enumerate(data):
        data[i] = np.roll(row, int(roll[i]))
    return data

def get_norm_tseries(tseries):
    ts = tseries - np.median(tseries)
    ts = ts/(1.4826*np.median(abs(ts-np.median(ts))))
    return ts

def load_train():
    BASEDIR = "./"
    l = glob.glob(os.path.join(BASEDIR,"./Train/*/*.npy"))
    train_data = np.zeros((len(l),NSUB,NBINS))

    #lines
    lines_list = sorted(os.listdir(os.path.join(BASEDIR,"Train","lines")))
    for i in range(len(lines_list)):
        train_data[i,:,:] = np.load(os.path.join(BASEDIR,"Train","lines",lines_list[i]))

    #curves
    curves_list = sorted(os.listdir(os.path.join(BASEDIR,"Train","curves")))
    for i in range(len(curves_list)):
        train_data[len(curves_list)+i,:,:] = np.load(os.path.join(BASEDIR,"Train","curves",curves_list[i]))

    y_train = np.concatenate((np.zeros((len(lines_list))),np.ones((len(curves_list)))))


    return train_data,y_train


def load_test():
    BASEDIR = "./"
    l = glob.glob(os.path.join(BASEDIR,"./Test/*/*.npy"))
    train_data = np.zeros((len(l),NSUB,NBINS))

    #lines
    lines_list = sorted(os.listdir(os.path.join(BASEDIR,"Test","lines")))
    for i in range(len(lines_list)):
        train_data[i,:,:] = np.load(os.path.join(BASEDIR,"Test","lines",lines_list[i]))

    #curves
    curves_list = sorted(os.listdir(os.path.join(BASEDIR,"Test","curves")))
    for i in range(len(curves_list)):
        train_data[len(curves_list)+i,:,:] = np.load(os.path.join(BASEDIR,"Test","curves",curves_list[i]))

    y_train = np.concatenate((np.zeros((len(lines_list))),np.ones((len(curves_list)))))


    return train_data,y_train
