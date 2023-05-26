# -*- coding: utf-8 -*-
"""
@author: Tristhal Parasram

Convolution Demo
This program displays an animation of two functions being convolved together.
Custom user-defined functions are supported.
 

-- Instructions --
This demo has several sections to be run in spyder or similar IPython based IDE

Spyder can be obtained by installing the Anaconda distribution of
 python https://www.anaconda.com/products/distribution then a program
 called "Spyder", "Spyder (anaconda3)" or something similar will be available.

There are 4 sections
1 - Function definitions
    In this section the functions to be used are defined. Some common functions 
    are provided, including an example which combines two other functions. You 
    are encouraged to create your own functions. 
    The last portion of this section plots a function so that you can check if 
    they are as expected.
    
2 - Setting the parameters for the convolution 
    In this section you will choose which functions to convolve as well as
    the parameters of the animation. The start and end value can be selected
    as well as a value where the animation will pause. Simply input the value
    at which you wish the animation to pause.

Nothing after this point needs to be modified

3 - Plotting the functions
    Simply run this section. The two functions being convolved are plotted as 
    f and g, so you can check to ensure your functions are correct. 
    
4 - Running the animation
    Run this section to see the animation. 
    *Remember to close the amination before running another one
    *Remember to adjust the y_min if your function is negative like a sine

5 - Plot the results at the pause points
    Run this section to obtain a plot at each of the specified pause points
    which can then be saved.
    
Note: to run a section you can press ctrl + enter or right click the area and
 select "run cell". You can also just run the whole file with f5 or the green 
 run arrow
Note: If the plotting/program stops working try closing the console 
 (hitting the x) or restarting it (right click on the "Console" tab on the 
 right). If that fails you can restart Spyder.
Note: The x-axis is supposed to extend to infinity, but that is not adding 
 extra info for space-limited functions. If the function is not space-limited
 there can be errors at the edges.

"""
#%% 1 - Some usefull functions as examples
# You can right click in a black space and click run cell to run each block in spyder
# You can also hit ctrl+enter while the area is highlighted
# You could also just run the whole file with the green play/run button above
# Imports. Do not change the following 5 lines.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
plt.close('all')  # Closes all plots

# Define functions. Modify and/or add new functions as you wish.
def box(x):
    T = 0.5
    return (x>-T) * (x<T) * 1.0

def step(x):
    return (x > 0) * 1.0

def biphasic_unitary_step(x):
    return box(x-0.5)-box(x-1.5)

def exponential(x):
    return np.exp(x)

def triangle(x):
    # Triangle with width 1
    y = ((x+1) * step(+1) -  2*x*step(x))*box(1/2*x)
    return y

def exponential_decay(x):
    return np.exp(-x)

def positive_exponential_decay(x):
    ''' Exponential function which is 0 for x<0'''
    return np.exp(-x) * step(x)

def sinusoid_1_period(x):
    period = np.pi  # set the period of the sin. could make smaller or larger
    box_stretch = np.pi  #1 period wide
    box_shift = box_stretch/2  # The box should be shifted so it starts at 0 instead of -0.5
    
    y = np.sin(x*(2*np.pi)/period) * box(1/box_stretch*(x-box_shift))
    return y

def sinusoid_3_period_phase(x):
    period = 1/3*np.pi  # set the period of the sine. could make smaller or larger
    phase_shift = 0  # 180 degree phase shift. could change this
    box_stretch = np.pi  # the box goes from 0 to pi to select only part of the sine
    
    box_shift = box_stretch/2  # The box should be shifted so it starts at 0
    y = np.sin(x*(2*np.pi)/period + phase_shift) * box(1/box_stretch*(x-box_shift))
    return y

def sinusoid_3_period_phase_shifted(x):
    period = 1/3*np.pi  # set the period of the sine. could make smaller or larger
    phase_shift = np.pi  # 180 degree phase shift. could change this
    box_stretch = np.pi  # the box goes from 0 to pi to select only part of the sine
    
    box_shift = box_stretch/2  # The box should be shifted so it starts at 0
    y = np.sin(x*(2*np.pi)/period + phase_shift) * box(1/box_stretch*(x-box_shift))
    return y

# This is a template to write your own function. You can write multiple and use them
#  for f(x) and g(x) in the next section for the convolution
# Replace the x**2 * box(1/2*x) with whatever you want

def your_function(x):
    # quadratic * stretched box
    y_value = x**2 * box(1/2*x)
    return y_value



# Sample code to plot your function
t = np.linspace(-5, 5, 1000)
plt.figure()  # Make a figure
plt.plot(t, sinusoid_3_period_phase_shifted(t))  # This is where you set the function you want to plot
plt.show()  # displays the plot in the plotting menu to the right, or it pops out


#############################################################
#%% 2 - Setting the parameters for the convolution animation#
#############################################################
# This %matplotlib qt5 turns on the popout plots. Type %matplotlib inline to go back to normal
# This line is not python code but rather an instruction to the ipython console
# As such the red x due to the syntax error is expected and a warning will appear
# the first time you run it.
%matplotlib qt5

# Selecting your functions to convolve
f = box  # Change f & g to whatever functions you want to convolve
g = triangle  # You can use your own function defined above

# Parameters for t axis
t_min = -10   # lower limit of x axis 
t_max = 10    # higher limit of x axis 
y_min = -1.5    # Lower limit of y axis
y_max = 2  # higher limit of y axis

# Animation settings
# pause_at_t = 0  # t value to pause animation. This is the x axis value.
pause_at_t = [-1.5, 0.0, 1.5, 3]  # An example of pause_at_t which pauses at multiple t values
pause_duration = 3  # How long (seconds) to pause for
pause = True  # Will pause at the specified t value(s) when set to True
steps = 2001  # The number of steps in the animation. The x axis is discretized into this number of points.
# If "steps" is set to small, a coarse resoution on x axis means you may miss the point pause_at_t and the pause occurs at its nearest neighbor.
delay_between_frames = 15  # Specifies how many ms between each frame (lower=faster)
frames_skipped = 8  # Number of frames to skip. Improves performance. Higher = faster.


## Beyond this point you only need to run the sections without changing any parameters 
#%% 3 - Plotting the functions selected
x = np.linspace(t_min, t_max, steps)
t = np.linspace(t_min, t_max, steps)

# Plotting f(x) and g(x)
plt.figure()  # Make a figure
plt.plot(x, f(x), 'r', label='f(t)')  # x=x values, f(x)=y values, label adds a label for the legend
plt.plot(x, g(x), 'b--', label='g(t)')  # x=x values, g(x)=y values, label adds a label for the legend
plt.ylim(y_min, y_max)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.legend()  # shows the legend
plt.show()  # displays the plot in the plotting menu to the right, or it pops out


#%% 4 - Displaying the animation for f * g
%matplotlib qt5
# Perform the convolution
f_conv_g = np.convolve(f(x), g(x), mode='same') * (x[1]-x[0])

# Figure out which frame to pause on
pause_frames = None
if pause:
    pause_frames = []
    if np.size(pause_at_t) == 1:
        pause_frames.append(np.argmin(np.abs(t-pause_at_t))+1)
    else:
        for pt in pause_at_t:
            pause_frames.append(np.argmin(np.abs(t-pt))+1)

# Function which updates the plot
def animate(i, t, ax, pause_frames=None):
    # print(t[i], i)
    f_line, = ax.plot(t, f(t), 'r', label='f(t)')
    area_line, = ax.fill(t, (g(-(t-t[i]))*f(t)), 'purple', alpha=0.7)
    g_line, = ax.plot(t, g(-(t-t[i])), 'b')
    line, = ax.plot(x[:(i+1)], f_conv_g[:(i+1)], color='k')
    if pause_frames is not None:
        if i in pause_frames:
            time.sleep(pause_duration)
    return line, f_line, g_line, area_line
    

fig, ax = plt.subplots()

# Adding static components
ax.set_ylim(y_min, y_max)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylabel('Amplitude')
ax.set_xlabel('t')


# addling lines for the legend
ax.plot(0, 0, 'r', label='f(t)')
ax.plot(0, 0, 'b', label='g(t)')
ax.plot(0, 0, 'k', label='f(t)*g(t)')
ax.fill(0, 0, 'purple', alpha=0.7, label='area of f(t)g(t)')
ax.legend(loc='upper left')

# Set up the indices to be plotted if it is not there
frame_range = np.arange(0, steps, frames_skipped)

# Insert the frame on which to pause
for pause_frame in pause_frames:
    if pause_frame not in frame_range:
        for i in range(len(frame_range)):
            if frame_range[i] > pause_frame:
                frame_range = np.insert(frame_range, i, pause_frame)
                break
            
    # Insert the frame before the pause if it is not there
    if pause_frame-1 not in frame_range:
        for i in range(len(frame_range)):
            if frame_range[i] > pause_frame-1:
                frame_range = np.insert(frame_range, i, pause_frame-1)
                break
end_pause_index = frame_range[-1]
# create the actual animation    
ani = animation.FuncAnimation(
    fig, lambda j: animate(j, t, ax, pause_frames), frames=frame_range,
    interval=delay_between_frames, blit=True, save_count=1)#, cache_frame_data=False)
plt.show()

#%% 5 Plot the results at the pause points
for i in pause_frames:
    fig, ax = plt.subplots()
    ax.plot(t, f(t), 'r', label='f(t)')
    ax.fill(t, (g(-(t-t[i]))*f(t)), 'purple', alpha=0.7, label='area of f(t)g(t)')
    ax.plot(t, g(-(t-t[i])), 'b', label='g(t)')
    ax.plot(x[:(i+1)], f_conv_g[:(i+1)], color='k', label='f(t)*g(t)')
    ax.legend(loc='upper left')
    plt.show()