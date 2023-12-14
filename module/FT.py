import numpy
import scipy
import matplotlib.pyplot as plt

from typing import Tuple, Any



def fourier(img:numpy.ndarray)->None:
    """
        Function that computes Fourier transform of an image.
        Input:
            img - image
        Output:
            None
        Other.
    		# https://docs.scipy.org/doc/scipy/tutorial/fft.html#and-n-d-discrete-fourier-transforms
    		# https://numpy.org/doc/stable/reference/routines.fft.html
    """
    x = scipy.fft.fftn(img)
    x = scipy.fft.fftshift(x)

    # plot phase and magnitude
    magnitude = numpy.abs(x) #numpy.sqrt(xreal**2 + ximag**2) 
    phase = numpy.arctan2(numpy.imag(x),numpy.real(x))  # numpy.angle(x)

    # reconstruct image
    y = magnitude * numpy.exp(1j*phase)
    y = scipy.fft.ifftshift(y)
    y = scipy.fft.ifftn(y) 
    y = numpy.real(y)
    y = numpy.clip(y, 0, 255).astype(numpy.uint8)
    plt.imshow(y)
    plt.show()



def hardthresholding(img:numpy.ndarray, threshold:float)->numpy.ndarray:
    """
        Function that performs hard thresholding.
        Input:
            img - image
            threshold - 
        Output:     
            image (threshold)
    """
    x = scipy.fft.fftn(img)
    #x = scipy.fft.fftshift(x)

    magnitude = numpy.abs(x)
    phase = numpy.arctan2(numpy.imag(x),numpy.real(x)) # numpy.angle(x)

    threshold *= numpy.mean(magnitude)
    x[numpy.where(magnitude < threshold)] = 0 #numpy.where(magnitude > threshold)

    magnitude = numpy.abs(x)
    phase = numpy.arctan2(numpy.imag(x),numpy.real(x))

    y = magnitude * numpy.exp(1j*phase)
    #y = scipy.fft.ifftshift(y)
    y = scipy.fft.ifftn(x) 
    y = numpy.real(y)
    y = numpy.clip(y, 0, 255).astype(numpy.uint8)
    return y



def IdealLowPassFilter(img:numpy.ndarray, D0:float)->numpy.ndarray:
    """
        Function that returns an Ideal Lowpass filter.
        Input:
            img - image
            D0 - cutoff frequency
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2)  

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
            if D(u,v) <= D0:
                H[u,v] = 1
            else:
                H[u,v] = 0
    return H

def ButterworthLowPassFilter(img:numpy.ndarray, D0:float, n:int)->numpy.ndarray:
    """
        Function that returns a Butterworth Lowpass filter.
        Input:
        Input:
            img - image
            D0 - cutoff frequency
            n - order
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2)  
    Butterworth = lambda u,v: 1/(1 + (D(u,v)/D0)**(2*n))

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
           H[u,v] = Butterworth(u,v)
    return H

def GaussianLowPassFilter(img:numpy.ndarray, sigma:float)->numpy.ndarray:
    """
        Function that returns an Gaussian Lowpass filter.
        Input:
            img - image
            sigma - cutoff frequency
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2)  
    gaussian = lambda u,v: numpy.exp(-D(u,v)**2/(2*sigma**2))

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
           H[u,v] = gaussian(u,v)
    return H

def IdealHighPassFilter(img:numpy.ndarray, D0:float)->numpy.ndarray:
    """
        Function that returns an Ideal Highpass filter.
        Input:
            img - image
            D0 - cutoff frequency
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2) 

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
            if D(u,v) <= D0:
                H[u,v] = 0
            else:
                H[u,v] = 1
    return H

def ButterworthHighPassFilter(img:numpy.ndarray, D0:float, n:int)->numpy.ndarray:
    """
        Function that returns a Butterworth Highpass filter.
        Input:
        Input:
            img - image
            D0 - cutoff frequency
            n - order
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2)  
    Butterworth = lambda u,v: 1/(1 + (D0/D(u,v))**(2*n))

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
           H[u,v] = Butterworth(u,v)
    return H


def GaussianHighPassFilter(img:numpy.ndarray, sigma:float)->numpy.ndarray:
    """
        Function that returns an Gaussian Highpass filter.
        Input:
            img - image
            sigma - cutoff frequency
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2) 
    gaussian = lambda u,v: numpy.exp(-D(u,v)**2/(2*sigma**2))

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
           H[u,v] = 1-gaussian(u,v)
    return H

def LaplacianFilter(img:numpy.ndarray, c:float)->numpy.ndarray:
    """
        Function that returns an Gaussian Laplacian filter.
        Input:
            img - image
            c - constant
        Output:
            filter
    """
    P = img.shape[0]
    Q = img.shape[1]
    D = lambda u,v: numpy.sqrt((u-P/2)**2 + (v-Q/2)**2)  

    H = numpy.zeros((P,Q))
    for u in range(P):
        for v in range(Q):
           H[u,v] = 1+c*(u**2+v**2)
    return H



def ftfiltering(img:numpy.ndarray, filters:str, *args: Tuple[Any])->numpy.ndarray: # mode:str
    """
        Function that ...
        Input:
        Output:
    """
    # TERMINER !!! - case of padding (image)
    match filters:
        case "lowpass":
            H = IdealLowPassFilter(img, float(args[0]))
        case "blowpass":
            H = ButterworthLowPassFilter(img, float(args[0]), float(args[0]))
        case "glowpass":
            H = GaussianLowPassFilter(img, float(args[0]))
        case "highpass":
            H = IdealHighPassFilter(img, float(args[0]))
        case "bhighpass":
            H = ButterworthHighPassFilter(img, float(args[0]), float(args[0]))
        case "ghighpass":
            H = GaussianHighPassFilter(img, float(args[0]))
        case _:
            raise Exception("\n[-]Error: Unknown type of filter.")

    match len(img.shape):
        case 2:
            pass
        case 3:
            h = numpy.zeros((H.shape[0], H.shape[1], img.shape[2]))
            for i in range(img.shape[2]):
                h[:,:, i] = H  
            H = h             
        case _:
            raise Exception("\n[-]Error: Unknown size of image.")

    F = scipy.fft.fftn(img)
    #x = scipy.fft.fftshift(x)

    Fphase = numpy.arctan2(numpy.imag(F),numpy.real(F))

    # perform filtering
    G = numpy.abs(H)*numpy.abs(F)* numpy.exp(1j*numpy.angle(F))

    #y = scipy.fft.ifftshift(G)
    y = scipy.fft.ifftn(G) 
    y = numpy.real(y)
    y = numpy.clip(y, 0, 255).astype(numpy.uint8)
    return y






