# Image Processing
Toolbox to perform image processing.

### Documentation

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


