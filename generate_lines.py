from __future__ import print_function
from utils import *

NBINS = 256
NSUB = 72
NLINES = 5000
NLINES_TEST = 500

if __name__ == "__main__":
    print("Generating lines...")
    o = open("./lines_train_description.txt", "a")
    o.write("#N snr width a b c\n")
    for i in range(NLINES):
        a_range = [0]
        b_range = [-7, 7]
        c_range = [-NBINS/2, +NBINS/2]
        width_range = [0.6, 5]
        snr_range = [15, 60]

        a,b,c,WIDTH,SNR = gen_rand_vars(a_range, b_range, c_range,
                width_range, snr_range)


        rolls = get_sub_rolls(NSUB, a, b, c)

        data = get_fake_data(NSUB, NBINS, WIDTH, SNR)
        data = roll_matrix(data, rolls)

        i_zfill = str(i).zfill(4)
        np.save("./Train/lines/line_%s"%i_zfill, data)
        o.write("%s %.2f %.2f %.4f %.4f %.4f\n" %
                (i_zfill, SNR, WIDTH, a, b, c))
    o.close()


    o = open("./lines_test_description.txt", "a")
    o.write("#N snr width a b c\n")
    for i in range(NLINES_TEST):
        a_range = [0]
        b_range = [-7, 7]
        c_range = [-NBINS/2, +NBINS/2]
        width_range = [0.6, 5]
        snr_range = [15, 60]

        a,b,c,WIDTH,SNR = gen_rand_vars(a_range, b_range, c_range,
                width_range, snr_range)


        rolls = get_sub_rolls(NSUB, a, b, c)

        data = get_fake_data(NSUB, NBINS, WIDTH, SNR)
        data = roll_matrix(data, rolls)

        i_zfill = str(i).zfill(4)
        np.save("./Test/lines/line_%s"%i_zfill, data)
        o.write("%s %.2f %.2f %.4f %.4f %.4f\n" %
                (i_zfill, SNR, WIDTH, a, b, c))
    o.close()
