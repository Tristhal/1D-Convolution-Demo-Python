# 1D-Convolution-Demo-Python
This program visualizes the discrete linear convolution of two functions using Matplotlib. Users can define custom input functions. The program generates an animation illustrating the convolution process, with the option to halt the animation at specific time steps and save those frames as separate images. Additionally, the full animation, excluding any programmed stops, can be exported as a GIF. The convolution is computed using NumPy.
<h3 align="center">
Animation showing the convolution
</h3>
<p align="center">
  <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/animation.gif">
</p>

 | Functions to be convolved | During the convolution | After the convolution |
| --- | --- | --- |
| <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_1.png"> | <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_2.png"> | <img src="https://github.com/Tristhal/1D-Convolution-Demo-Python/blob/master/images/Figure_3.png"> |

## Requirements
Matplotlib and NumPy are required to run this program. This program is only compatible with Python 3 and above. The animated plot uses the Qt5 GUI and was tested in the Spyder IDE.

## Setup Instructions
### Spyder
Open the .py or the .ipy file in python. Ensure the Qt5 backend is enabled by using the %matplotlib qt5 command in the console. Execute the code section by section changing the functions or parameters where necessary. 

### Command Line
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



