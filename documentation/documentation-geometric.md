# Image Processing
Toolbox to perform image processing.

### Documentation

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





