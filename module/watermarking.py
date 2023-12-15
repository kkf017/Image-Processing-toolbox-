import numpy
import matplotlib.pyplot as plt




def cover(img1:numpy.ndarray, img2:numpy.ndarray)->numpy.ndarray:
    """
        Function that ...
        Input:
        Output:     
    """
    y = numpy.zeros(img1.shape)

    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            print("\n")
            print("Red channel {},{}: {} {}, {} {}.".format(i,j, img1[i,j,0], "{0:b}".format(img1[i,j,0]), img2[i,j,0], "{0:b}".format(img2[i,j,0])))
            print("Green channel {},{}: {} {}, {} {}.".format(i,j, img1[i,j,1], "{0:b}".format(img1[i,j,1]), img2[i,j,1], "{0:b}".format(img2[i,j,1])))
            print("Blue channel {},{}: {} {} {}, {} {}.".format(i,j, img1[i,j,2], bin(img1[i,j,2]), bin(img1[i,j,2])[2:], img2[i,j,2], "{0:b}".format(img2[i,j,2])))


            print(int("{0:b}".format(img1[i,j,0])[:5]+"{0:b}".format(img2[i,j,0])[:3], 2))
            print(int("{0:b}".format(img1[i,j,1])[:6]+"{0:b}".format(img2[i,j,2])[:2],2))
            print(int("{0:b}".format(img1[i,j,2])[:3]+"{0:b}".format(img2[i,j,1])[:3]+"{0:b}".format(img2[i,j,2])[2:4],2))

            y[i,j,0] = int("{0:b}".format(img1[i,j,0])[:5]+"{0:b}".format(img2[i,j,0])[:3], 2)
            y[i,j,1] = int("{0:b}".format(img1[i,j,1])[:6]+"{0:b}".format(img2[i,j,2])[:2],2)
            y[i,j,2] = int("{0:b}".format(img1[i,j,2])[:3]+"{0:b}".format(img2[i,j,1])[:3]+"{0:b}".format(img2[i,j,2])[2:4],2)


            y[i,j,0] = int("0b"+bin(img1[i,j,0])[2:][:5]+bin(img2[i,j,0])[2:][:3], 2)
            y[i,j,1] = int("0b"+bin(img1[i,j,1])[2:][:6]+bin(img2[i,j,2])[2:][:2],2)
            y[i,j,2] = int("0b"+bin(img1[i,j,2])[2:][:3]+bin(img2[i,j,1])[2:][:3]+bin(img2[i,j,2])[2:][2:4],2)

            #input()
   
    y = numpy.clip(y, 0, 255).astype(numpy.uint8)
    plt.imshow(y)
    plt.show()
    return img1



def recover(img:numpy.ndarray)->numpy.ndarray:
    return img
