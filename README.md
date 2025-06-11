# 1D-Convolution-Demo-Python

This program displays an animation, using Matplotlib, of two functions being convolved together. Custom user-defined functions are supported. The Matplotlib animation can be made to stop at different time points and those images can be saved seperately. The animation can also be saved as a gif excluding the programmed stop. A discrete, linear convolution is performed using NumPy.
<h3 align="center">
Animation showing the convolution
</h3>
<p align="center">
  <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/animation.gif">
</p>

 | Functions to be convolved | During the convolution | After the convolution |
| --- | --- | --- |
| <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_1.png"> | <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_2.png"> | <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_3.png"> |

Matplotlib and NumPy are required to run this program. This program is only compatible with Python 3 and above. The animated plot uses the Qt5 GUI and was tested in the Spyder IDE.

### Setup Instructions

Run the following commands:
```
pip install numpy
pip install matplotlib
python convolution_demo.py
```

If running a machine that has installations for both Python 2 and Python 3, you may need to run the following instead:
```
python3 -m pip install numpy
python3 -m pip install matplotlib
python3 convolution_demo.py
```



