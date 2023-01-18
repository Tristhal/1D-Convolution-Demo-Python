# -*- coding: utf-8 -*-
"""
@author: Tristhal Parasram

Convolution Demo
This program displays an animation of two functions being convolved together.
Custom user-defined functions are supported and the. A discrete, 
linear convolution is performed using numpy.
 

-- Instructions --
This demo has several sections made to be run in spyder or similar IPython based IDE

Spyder can be obtained by installing the Anaconda distribution of
 python https://www.anaconda.com/products/distribution then a program
 called "Spyder", "Spyder (anaconda3)" or something similar will be available.

There are 4 sections
1 - Function definitions
    In this section the functions to be used are defined. There are some
    commonly used functions used. There is also an example function which combines
    two other functions so that you can write your own. There is also code
    included to plot your functions to make sure they are as you expect.
    
2 - Setting the parameters for the convolution 
    In this section you will choose which functions to convolve as well as
    the parameters of the animation. The start end end time can be selected
    as well as a time where the animation will pause. Simply input the time
    at which you wish the animation to pause.

Nothing after this point needs to be modified

3 - Plotting the functions
    Simply run this section. In this section the two functions being convolved 
    are plotted f * g. Here you can check to ensure your functions are correct 
    and you have selected an apropriate x (time) axis.
    
4 - Running the animation
    Run this section to see the animation.
    
Note: to run a section you can press ctrl + enter or right click the area and
 select "run cell". You can also just run the whole file with f5 or the green 
 run arrow
"""
#%% 0 - Imports (Must run first)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

#%% 1 - Some usefull functions as an example
# You can right click in a black space and click run cell to run each block in spyder
# You can also hit ctrl+enter while the area is highlighted
# You could also just run the whole file with the green play/run button above
def box(x):
    T = 0.5
    return (x>-T) * (x<T) * 1.0

def step(x):
    return (x > 0) * 1.0

def exponential(x):
    return np.exp(x)

def triangle(x):
    # Triangle with width 1
    y = ((x+1) * step(+1) -  2*x*step(x))*box(1/2*x)
    return y

def exponential_decay(x):
    return exponential(-x)


# This is a template to write your own function. You can write multiple and use them
#  for f(x) and g(x) in the next section for the convolution
# Replace the x**2 with whatever you want
# You can look up common functions.
# Some common ones np.exp(x), np.sin(x), np.cos(x)
# 
def your_function(x):
    # quadratic * stretched box
    y_value = x**2 * box(1/2*x)
    return y_value



# Sample code to plot your function
t = np.linspace(-5, 5, 1000)
plt.figure()  # Make a figure
plt.plot(t, triangle(t))  # This is where you set the function you want to plot
plt.show()  # displays the plot in the plotting menu to the right, or it pops out


#############################################################
#%% 2 - Setting the parameters for the convolution animation#
#############################################################
# This %matplotlib qt5 turns on the popout plots. Type %matplotlib inline to go back to normal
%matplotlib qt5

# Selecting your functions to convolve
f = box  # Change these to whatever functions you want to convolve
g = triangle  # You can define your own above and plot them

# Parameters for time axis
t_min = -5   # Shortest time to be plotted
t_max = 5    # Longest time point to be plotted
y_min = 0    # bottom of y axis
y_max = 1.5  # top of y axis

# Animation settings
pause_at_time = 0.5        # Time to pause animation to save different 
pause_duration = 5         # How long (seconds) to pause for
pause = True               # Will pause at time when set to True
steps = 2001               # The number of steps in the animation and time points on the x axis
delay_between_frames = 15  # Specifies how many ms between each fram (lower=faster)
frames_skipped = 8         # Number of frames to skip. Improve sperformance. Higher = faster.


## Beyond this point you just have to run the sections not change any parameters 
#%% 3 - Plotting the functions selected
x = np.linspace(t_min, t_max, steps)
t = np.linspace(t_min, t_max, steps)

# Plotting f(x) and g(x)
plt.figure()  # Make a figure
plt.plot(x, f(x), label='f(x)')  # x=x values, f(x)=y values, label adds a label for the legend
plt.plot(x, g(x), label='g(x)')  # x=x values, g(x)=y values, label adds a label for the legend
plt.ylim(y_min, y_max)
plt.legend()  # shows the legend
plt.show()  # displays the plot in the plotting menu to the right, or it pops out


#%% 4 - Displaying the animation for f * g
%matplotlib qt5
# Perform the convolution
f_conv_g = np.convolve(f(x), g(x), mode='same') * (x[1]-x[0])

# Figure out which frame to pause on
pause_frames = None
if pause:
    pause_frames = np.argmin(np.abs(t-pause_at_time))+1

# Function which updates the plot
def animate(i, t, ax, pause_frames=None):
    # print(t[i], i)
    area_line, = ax.fill(t, (g(-(t-t[i]))*f(t)), 'purple', alpha=0.7)
    g_line, = ax.plot(t, g(-(t-t[i])), 'b')
    line, = ax.plot(x[:(i+1)], f_conv_g[:(i+1)], color='k')
    if pause_frames is not None:
        if i == pause_frames:
            plt.pause(pause_duration)
    return line, f_line, g_line, area_line
    

fig, ax = plt.subplots()

# Adding static components
ax.set_ylim(y_min, y_max)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylabel('Amplitude')
ax.set_xlabel('Time')

# Plotting f since it is static
f_line, = ax.plot(t, f(t), 'r', label='f(t)')

# addling lines for the legend
ax.plot(0, 0, 'b', label='g(t)')
ax.plot(0, 0, 'k', label='f(t)*g(t)')
ax.fill(0, 0, 'purple', alpha=0.7, label='area of f(t)g(t)')
ax.legend(loc='upper right')

# Set up the indices to be plotted if it is not there
frame_range = np.arange(0, steps, frames_skipped)

# Insert the frame on which to pause
if pause_frames not in frame_range:
    for i in range(len(frame_range)):
        if frame_range[i] > pause_frames:
            frame_range = np.insert(frame_range, i, pause_frames)
            break
        
# Insert the frame before the pause if it is not there
if pause_frames-1 not in frame_range:
    for i in range(len(frame_range)):
        if frame_range[i] > pause_frames-1:
            frame_range = np.insert(frame_range, i, pause_frames-1)
            break
end_pause_index = frame_range[-1]
# create the actual animation    
ani = animation.FuncAnimation(
    fig, lambda j: animate(j, t, ax, pause_frames), frames=frame_range,
    interval=delay_between_frames, blit=True, save_count=50, cache_frame_data=False)
plt.show()