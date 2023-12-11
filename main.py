import os
import sys
import numpy
import matplotlib.image as mpimg


sys.path.insert(1,'./module/')

from display import *
from transform import *
from histogram import *
from filter import *

from typing import List


# STreamlit (website)


def main(argv:List[str], argc:int)->None:
    filename = argv[-1]
    exists(filename)
    img = mpimg.imread(filename)

    display(img,"Original image".format(img.shape))
    displayRGB(img)
    grey = greyscale(img)
    display(grey, "Grey image")

    # manage arguments
    #string.replace('g', '')
    #if '' in sys.argv[]



if __name__ == "__main__":

    main(sys.argv, len(sys.argv))
