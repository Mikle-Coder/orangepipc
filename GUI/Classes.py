from tkinter.ttk import *
from tkinter import *
import os
import time



def Format(value, formatStyle):
    if(formatStyle == "time" ):
        return '{:02}:{:02}'.format(0, value)
    if(formatStyle == "frequency"):
        return str(value) + " КГц"
    if(formatStyle == "temperature"):
        return str(value) + " ℃"

class TabModel:
    
    def __init__(self, tabtext, labeltext, notebook, colors, paramRange, formatStyle):
        self.frame = Frame(notebook,bg=colors[0])
        notebook.add(self.frame, text=tabtext)
        self.label = None
        self.value = paramRange.Min

        tableWeight=2
        tableHeight=3

        for c in range(tableHeight): self.frame.columnconfigure(index=c, weight=1)
        for r in range(tableWeight): self.frame.rowconfigure(index=r, weight=1)

        textlabel = Label(self.frame, text=labeltext, font=25, background=colors[0], width=100)
        textlabel.grid(row=0,columnspan=2,sticky=S)

        self.label = Label(self.frame, text=Format(self.value, formatStyle), background=colors[0], font=35)
        self.label.grid(row=1, columnspan=2,sticky=S)

        self.control = Control(self.frame, self.value, self.label, colors, paramRange, formatStyle)



class Control:

    def __init__(self, frame, value, label, colors, paramRange, formatStyle):
        self.holding_trigger = False
        self.running = False
        self.jobid = None

        self.frame = frame
        self.value = value
        self.label = label
        self.formatStyle = formatStyle

        self.paramRange = paramRange

        direction = ["+", "-"]
        for n in range(len(direction)):
            button = Button(self.frame, text=direction[n], font=25, bg=colors[1], borderwidth=0, width=10)
            button.grid(row=2, column=n, pady= 50,sticky=N)
            button.bind('<ButtonPress-1>', lambda event, direction=direction[n]: self.start_motor(direction))
            button.bind('<ButtonRelease-1>', lambda event: self.stop_motor())

    def start_motor(self, direction):
        self.move(direction)

    def stop_motor(self):
        self.frame.after_cancel(self.jobid)
        self.holding_trigger=False

    def move(self, direction):
        if(direction=="+" and self.value < self.paramRange.Max):
            self.value += self.paramRange.Pitch
        elif(direction=="-" and self.value > self.paramRange.Min):
            self.value -= self.paramRange.Pitch

        self.label.configure(text = Format(self.value, self.formatStyle))

        time = 500
        if(self.holding_trigger==True):
            time=50
        else:
            self.holding_trigger=True

        self.jobid = self.frame.after(time, self.move, direction)

class ParamRange:

    def __init__(self, _min, _max, pitch):
        self.Min = _min
        self.Max = _max
        self.Pitch = pitch
   