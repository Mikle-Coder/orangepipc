from tkinter.ttk import *
from tkinter import *
import os
import time

import Classes

color1='#ADADFF'
color2='#D8D8FF'
 
root = Tk()
root.configure(bg=color1)
weight = 320
height = 240
root.geometry(f"{weight}x{height}")

root.wm_attributes('-fullscreen','true')

style = Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')
notebook = Notebook(root, style='lefttab.TNotebook', width=weight-55, height=height)


signalform_frame = Frame(notebook, bg=color1)
notebook.add(signalform_frame, text='Форма')
signalform_label = None
signalform_value = ""

path = os.getcwd() + r"\Images"
images=[
    PhotoImage(file = path + r"\1-sin.png"),
    PhotoImage(file = path + r"\2-tri.png"),
    PhotoImage(file = path + r"\3-rect.png"),
    PhotoImage(file = path + r"\4-saw.png"),
    ]

def signalform_init():

    tableWeight=2
    tableHeight=3

    for c in range(tableHeight): signalform_frame.columnconfigure(index=c, weight=1)
    for r in range(tableWeight): signalform_frame.rowconfigure(index=r, weight=1)
    
    signalform_label = Label(signalform_frame, text="Форма сигнала:")
    signalform_label.grid(row=0, columnspan=2)

    counter=0
    for r in range(1, tableHeight):
        for c in range(tableWeight):
            btn = Button(signalform_frame,image=images[counter], borderwidth=0, bg=color2)
            btn.grid(row=r, column=c)
            counter+=1


temperature = None
frequency = None
timer = None
 
def init_all(): 
    signalform_init()
    colors = [color1, color2]
    temperature = Classes.TabModel('Тем-ра', 'Температура', notebook, colors, Classes.ParamRange(40, 70, 5), "temperature")
    frequency = Classes.TabModel("Час-та", "Частота", notebook, colors, Classes.ParamRange(20, 40, 5), "frequency")
    timer = Classes.TabModel("Таймер", "Таймер обратного отсчета", notebook, colors, Classes.ParamRange(0, 10, 1), "time")


init_all()
notebook.pack()
root.mainloop()







































