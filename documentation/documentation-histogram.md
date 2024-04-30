# Image Processing
Toolbox to perform image processing.

### Documentation

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


