import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog
import numpy as np
is_init = True

root = Tk()
#UI Settings#
bg_color = "#303138"
button_color = "#606060"
text_color = "#969696"
button_t_color = "#b3b2c5"
app_with = 1024
app_height = 720
reso = app_with, app_height
root.title("Storm3DVisualisator")
is_init = True
root.resizable(False, False)
root.configure(background = bg_color)
points = []

#Function to initialize a windows file selection box#
def winSelect():
    global loc
    loc = filedialog.askopenfilename(title="Select Save File", filetypes=(("storm3d", "*.storm3d"),))
    with open(loc, 'r') as f:
        for line in f:
            x, y, z = map(float, line.strip().split())
            points.append((x, y, z))

#Main page#
def saveSelect():
    saveSelect_label = Label(root, text="  Welcome to Storm3DVisualisator By CharlesAntoine  ", font=("Courier", 15), bg = bg_color, fg = text_color)
    saveSelect_label.grid(row=1, column = 1)
    #Select Button#
    saveSelect_button = Button(root, text = "Select a storm3d file", padx = 50, pady = 5, command = winSelect, bg = button_color, fg = button_t_color)
    saveSelect_button.grid(row = 2, column = 1)
    #Exit Button#
    exit_button = Button(root, text="Exit", padx = 50, pady = 5, command = exit, bg = button_color, fg = button_t_color)
    exit_button.grid(row = 4, column = 1)
    #Render Button#
    render_button = Button(root, text="Render!", padx = 50, pady = 5, command = render, bg = button_color, fg = button_t_color)
    render_button.grid(row = 3, column = 1)
def exit():
    root.destroy()
def render():
    global points
    points = np.array(points)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2])
    plt.show()

if is_init:
    saveSelect()
    is_init = False
root.mainloop()
