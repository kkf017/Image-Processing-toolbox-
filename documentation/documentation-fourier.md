# Image Processing
Toolbox to perform image processing.

### Documentationt
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

