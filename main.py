import os
import sys
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

sys.path.insert(1, './module/')

from func import main
from colors import *

from typing import List






if __name__ == "__main__":

    print("\033[{}mIMGMagic 1.0.".format("1;35"))

    main(sys.argv, len(sys.argv))

    print("\n\033[{}mUse --help to list all available options.".format("1;30"))

