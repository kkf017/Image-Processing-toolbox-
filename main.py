import os
import sys

from app.func import main

from typing import List


    # -
        # High pass filter
        # contrast adjustment 
        # negative
        # FT - Ideal low pass, Butterworth low pass, Gaussian low pass

    # Extra tools - Laplacian pyramid, pyramid denoising, wavelet decomposition/denoising





if __name__ == "__main__":

    print("\033[{}mIMGMagic 1.0.".format("1;35"))

    main(sys.argv, len(sys.argv))

    print("\n\033[{}mUse --help to list all available options.".format("1;30"))

