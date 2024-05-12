## IMGMagic Toolbox
Toolbox to perform image processing.


### Libraries
* Requires python>=3.5.
* Install numpy, scipy, matplotlib, pillow.


### Example
```python
import numpy
import matplotlib.image as mpimg
from PIL import Image
import imgmagic

	
filename = "img.jpeg"
img1 = mpimg.imread(filename)
img2 = numpy.copy(img1)

img2 = imgmagic.display.greyscale(img1)
	
im = Image.fromarray(img2)
if len(img2.shape) == 2:
	im = im.convert('L')
im.save("new.jpeg")
```

### Documentation

#### Display
This module contains functions to **display** an image.

###### Example 1
```python
img2 = imgmagic.display.greyscale(img1)
```


#### Geometric
This module contains functions to apply **geometric transforms** on an image.

###### Example 1
```python

img2 = imgmagic.geometric.crop(img1, (520,520), 75,75)
	
```

###### Example 2
```python
img2 = imgmagic.geometric.rotate(img1, 65)
	
```

###### Example 3
```python
img2 = imgmagic.geometric.flipping(img1)
```

###### Example 4
```python
img2 = imgmagic.geometric.reverse(img1)
```
###### Example 5
```python
img2 = imgmagic.geometric.scaling(img1, 0.25)
img2 = imgmagic.geometric.scaling(img1, 1.25)
```

#### Histogram
This module contains functions to perform **histogram enhancement** .

###### Example 1
```python
img2 = imgmagic.histogram.adjustContrast(img1)
```
###### Example 2
```python
imgmagic.histogram.equalization(img1)
```
###### Example 3
```python
imgmagic.histogram.negative(img1)
```


#### Filter
This module contains functions to perform **filtering**.

###### Example 1
```python
img2 = imgmagic.filter.GaussianNoise(img1, 125,0)
img2 = imgmagic.filter.SaltnPepperNoise(img1, 0.01)
```

###### Example 3
```python
filters =  {"lowpass", "highpass", "avg", "gauss"}
padding = {"reflect", "constant", "nearest", "mirror", "wrap"}

imgmagic.filter.filtering(img1, "lowpass", "reflect")
imgmagic.filter.filtering(img1, "avg", "wrap", 9)
```
###### Example 4
```python
filters =  {"laplacian", "sobel", "roberts"}
padding = {"reflect", "constant", "wrap"}

imgmagic.filter.sharpening(img1, "sobel", "wrap")
```
###### Example 5
```python
sub1 =  mpimg.imread("sub1.jpeg")
sub2 =  mpimg.imread("sub2.jpeg")

filters = {"laplacian", "sobel", "roberts"}

img2 = imgmagic.filter.crosscorrelation(sub1, "sobel", sub2)
```

#### Filter
This module contains functions to perform **FT filtering**.

###### Example 1
```python
img2 = imgmagic.fourier.ftfiltering(img1, "highpass", 145)
```
###### Example 2
```python
img2 = imgmagic.fourier.UnsharpMasking(img1, 145, 1)
```
###### Example 3
```python
img2 = imgmagic.fourier.HighFreqEmph(img1, 145, 1, 5)
```



### Manual

**imgmagic.display.greyscale(x: numpy.ndarray)**<br />
Function that converts image into greyscale.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **x : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to convert.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Returns the greyscale image.<br />


**imgmagic.geometric.crop(img:numpy.ndarray, x:Tuple[int], width:int, height:int)**<br />
 Function that crops an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to crop.<br />
&emsp;&emsp;&emsp;&emsp; **x : Tuple[int]**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Coordiates of starting point.<br />
&emsp;&emsp;&emsp;&emsp; **width : int**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Width of the cropped image.<br />
&emsp;&emsp;&emsp;&emsp; **height : int**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Height of the cropped image.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Cropped image.<br />

    
**imgmagic.geometric.rotate(img:numpy.ndarray, degree:float)**<br />
Function that rotates an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to rotate.<br />
&emsp;&emsp;&emsp;&emsp; **degree : int**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Angle of rotaion (degrees). This parameter can be positive or negative.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Rotated image.<br />

**imgmagic.geometric.flipping(img:numpy.ndarray)**<br />
Function that flips an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to rotate.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Flipped image.<br />

**imgmagic.geometric.scaling(img:numpy.ndarray, scale:float)**<br />
Function that scales an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to scale.<br />
&emsp;&emsp;&emsp;&emsp; **scale : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Factor of scaling (ex. 0.5, 1.25, 2...etc).<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Scaled image.<br />


**imgmagic.geometric.reverse(img:numpy.ndarray)**<br />
Function that reverts an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image to reverse.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Reverted image.<br />

**imgmagic.histogram.adjustContrast(img:numpy.ndarray)**<br />
Function that performs contrast stretching.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (with contrat stretching).<br />

**imgmagic.histogram.equalization(img:numpy.ndarray)**<br />
Function that performs histogram equalization.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (with equalization).<br />

**imgmagic.histogram.negative(img:numpy.ndarray)**<br />
Function that performs computes digital negative of an image.<br />
&emsp;&emsp;&emsp;&emsp;s = T( r ) = (L – 1) – r<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (negative).<br />

**imgmagic.filter.GaussianNoise(img:numpy.ndarray, mean:float, sigma:float)**<br />
Function that adds gaussian noise to an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **mean, sigma : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Parameters for gaussian distribution.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (with noise).<br />


**imgmagic.filter.SaltnPepperNoise(img:numpy.ndarray, prob:float)**<br />
Function that adds salt and pepper noise.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **prob : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Probability for salting (ex. 0.01 ...etc).<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (with noise).<br />

**imgmagic.filter.filtering(img:numpy.ndarray, types:str, mode:str, *args: Tuple[Any])**<br />
Function that perfoms filtering on an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **types : {"lowpass", "highpass", "avg", "gauss"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of filter.<br />
&emsp;&emsp;&emsp;&emsp; **mode : {"reflect", "constant", "nearest", "mirror", "wrap"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of padding.<br />
&emsp;&emsp;&emsp;&emsp; **args : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Extra arguments (optional). For instance, it can be:<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  n : size for avg filter<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (filtered).<br />


**imgmagic.filter.sharpening(img:numpy.ndarray, types:str, mode:str)**<br />
Function that perfoms sharpening on an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **types : {"laplacian", "sobel", "roberts"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of filter.<br />
&emsp;&emsp;&emsp;&emsp; **mode : {"reflect", "constant", "wrap"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of padding.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (filtered).<br />

**imgmagic.filter.crosscorrelation(img:numpy.ndarray, filters:str, sub:numpy.ndarray)**<br />
Function that find a subimage in an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **filters : {"laplacian", "sobel", "roberts"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of filter.<br />
&emsp;&emsp;&emsp;&emsp; **sub : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Subimage image.<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (found).<br />

**imgmagic.fourier.ftfiltering(img:numpy.ndarray, filters:str, *args: Tuple[Any])**<br />
Function that perfoms sharpening on an image.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **filters : {"lowpass", "blowpass", "glowpass", "highpass", "bhighpass", "ghighpass", "bandreject", "bandpass", "homomorphic"}**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Type of filter.<br />
&emsp;&emsp;&emsp;&emsp; **args : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Extra arguments (optional). For instance, it can be:<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  D0 : cutoff frequency for Ideal filter ("lowpass", "highpass")<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  D0, n : cutoff frequency, order for Butterworth filter ("blowpass", "bhighpass")<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; sigma : cutoff frequency for Gaussian filter ("glowpass", "ghighpass")<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image (filtered).<br />


**imgmagic.fourier.UnsharpMasking(img:numpy.ndarray, D0:int, k:int)**<br />
Function that performs Unsharp Masking and Highboost filtering.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **k : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Parameter:<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; k=1 - unsharp masking<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; k>1 - highboost filtering<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image.<br />


**imgmagic.fourier.HighFreqEmph(img:numpy.ndarray, D0:int, k1:int, k2:int)**<br />
Function that performs High-frequency emphasis.<br />
&emsp;&emsp; **Parameters**:<br />
&emsp;&emsp;&emsp;&emsp; **img : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Input image.<br />
&emsp;&emsp;&emsp;&emsp; **k1, k2 : float**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Parameters:<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; k1=1<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; k2=1 - unsharp masking<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; k2>1  - highboost filtering<br />
&emsp;&emsp; **Returns**:<br />
&emsp;&emsp;&emsp;&emsp; **output : numpy.ndarray**<br />
&emsp;&emsp;&emsp;&emsp;&emsp; Image.<br />






