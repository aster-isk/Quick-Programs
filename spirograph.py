import math
import Tkinter as tk
import random
import PIL as pil
import os
import color_functions as clr

#Sliders For Size/Hole Position, Colorwheel Slider, Rainbow Button, Random Button
#Drawing that shows what the spirograph looks like 

root = tk.Tk()
root.wm_title('Spirograph')

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#Canvas
canvas1 = tk.Canvas(root, width=505, height=505, background='#FFFFFF')
canvas1.grid(row=0, rowspan=10, column=2)
canvas2 = tk.Canvas(root, width=505, height=505, background='#FFFFFF')
canvas2.grid(row=0, rowspan=10, column=3)
canvas1.create_oval(505, 505, 2, 2)

#Global Variables
r_int = tk.IntVar()
r_int.set(75)
p_int = tk.IntVar()
p_int.set(0)
w_int = tk.IntVar()
w_int.set(6)
m_int = tk.IntVar()
g_int = tk.IntVar()
b_int = tk.IntVar()

#Changes the spirograph components, radius of inner circle, width of pencil line
#color of pencil
#Takes the new integer values of each specified slider, activates when a slider
#is changed, is show on canvas1
def change_graph(new_intval):
    r = r_int.get()
    p = p_int.get()
    w = w_int.get() / 2
    hexcode = clr.hexstring([m_int.get(), g_int.get(), b_int.get()])
    
    canvas1.create_rectangle(510, 510, 0, 0, fill="white")
    canvas1.create_oval(505, 505, 2, 2, fill="white")
    canvas1.create_oval((2 * r), (250 + r), 0, (250 - r), fill = hexcode)
    canvas1.create_oval(((r*p/50) - w), (250 + (w)), ((r*p/50) + w), (250 - w), 
                        fill = "black", outline = "white")
    
#Draws spirograph with the given perameters on canvas2
def generate_spirograph():
    r = r_int.get()
    p = abs((r * p_int.get() / 50) - r)
    w = w_int.get() / 2
    hexcode = clr.hexstring([m_int.get(), g_int.get(), b_int.get()])
    graph_function(r, p, 0, hexcode, w)
    
def generate_rainbow():
    r = r_int.get()
    p = abs((r * p_int.get() / 50) - r)
    w = w_int.get() / 2
    graph_rainbow(r, p, 0, w)

def clear_canvas():
        canvas2.create_rectangle(510, 510, 0, 0, fill="white")
        
#takes a hex color code string, width int, x position and y position on the x-y plane,
#graphs that point with that width on the 0 - 500 canvas2
def graph_point(hexcode, w, x_1, y_1, x_2, y_2):
    canvas2.create_line((x_1 + 250), (y_1 + 250), (x_2 + 250),  (y_2 + 250), 
                        width = w, fill = hexcode)
    canvas2.create_oval((x_2 + 250 + w/2), (y_2 + 250 + w/2), (x_2 + 250 - w/2), 
                        (y_2 + 250 - w/2), fill = hexcode, outline = hexcode)
        
#Graphs spirograph according to functions y =(R-r)sin(rt/R)-psin((1-r/R)t)
#and x =(R-r)cos(rt/R)-pcos((1-r/R)t), where R = 250, r = r_int, p = |(rp/50)-r)|
#and t is variable angle of theta     
def graph_function(r, p, t, hexcode, width):
    start_x, start_y = spiro_function(r, p, 0)

    for i in range(t, (360 + t)):
        rad_1 = math.radians(i)
        rad_2 = math.radians(i + 1)
        x_1, y_1 = spiro_function(r, p, rad_1)
        x_2, y_2 = spiro_function(r, p, rad_2)
        graph_point(hexcode, width, x_1, y_1, 
                    x_2, y_2)

        if t > 360 and abs((start_x) - int(x_2)) == 0 and abs((start_y) - int(y_2)) == 0 :
            return
        
    graph_function(r, p, t + 360, hexcode, width)

def graph_rainbow(r, p, t, width):
    start_x, start_y = spiro_function(r, p, 0)

    for i in range(t, (360 + t)):
        rad_1 = math.radians(i)
        rad_2 = math.radians(i + 1)
        x_1, y_1 = spiro_function(r, p, rad_1)
        x_2, y_2 = spiro_function(r, p, rad_2)
        graph_point(clr.hexstring(clr.make_hue(rad_1/3.14159265)), width, x_1, y_1, 
                    x_2, y_2)
                    
        if t > 360 and abs((start_x) - int(x_2)) == 0 and abs((start_y) - int(y_2)) == 0 :
            return
        
    graph_rainbow(r, p, t + 360, width)

def spiro_function(r, p , t):
    x = (250 - r) * math.cos(r * t / 250) - p * math.cos((1 - r / 250) * t)
    y = (250-  r) * math.sin(r * t / 250) - p * math.sin((1 - r / 250) * t)
    return x, y 
    
#Sliders
radius_slider = tk.Scale(root, from_=1, to=245, variable=r_int, 
                orient=tk.HORIZONTAL, label='Radius', command=change_graph)
radius_slider.grid(row=0, column=0, sticky=tk.E)
pen_slider = tk.Scale(root, from_=1, to=100, variable=p_int, 
                orient=tk.HORIZONTAL, label='Pen Position', command=change_graph)
pen_slider.grid(row=1, column=0, sticky=tk.E)
width_slider = tk.Scale(root, from_=1, to=30, variable=w_int, 
                orient=tk.HORIZONTAL, label='Line Width', command=change_graph)
width_slider.grid(row=2, column=0, sticky=tk.E)
red_slider = tk.Scale(root, from_=1, to=255, variable=m_int, 
                orient=tk.HORIZONTAL, label='Red', command=change_graph)
red_slider.grid(row=0, column=1, sticky=tk.E)
green_slider = tk.Scale(root, from_=1, to=255, variable=g_int, 
                orient=tk.HORIZONTAL, label='Green', command=change_graph)
green_slider.grid(row=1, column=1, sticky=tk.E)
blue_slider = tk.Scale(root, from_=1, to=255, variable=b_int, 
                orient=tk.HORIZONTAL, label='Blue', command=change_graph)
blue_slider.grid(row=2, column=1, sticky=tk.E)

#Buttons
generate_button = tk.Button(root, text='Generate', command=generate_spirograph)
generate_button.grid(row=6, column=0)
rainbow_button = tk.Button(root, text='Rainbow', command=generate_rainbow)
rainbow_button.grid(row=6, column=1)
#save_button = tk.Button(root, text='Save')#, command=
#save_button.grid(row=8, column=0)
clear_button = tk.Button(root, text='Clear', command=clear_canvas)
clear_button.grid(row=7, column=0)

root.mainloop()