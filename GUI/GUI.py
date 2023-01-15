from tkinter.ttk import *
from tkinter import *
import  tkinter as tk
import os
from datetime import datetime
from w1thermsensor import W1ThermSensor as Sen
import Classes

class GUI:

    color1='#ADADFF'
    color2='#D8D8FF'
    colors = [color1, color2]

    root = Tk()
    root.configure(bg=color1)
    weight = 320
    height = 240
    root.geometry(f"{weight}x{height}")

    #root.wm_attributes('-fullscreen','true')

    style = Style(root)
    style.configure('lefttab.TNotebook', tabposition='wn')
    notebook = Notebook(root, style='lefttab.TNotebook', width=weight-55, height=height)

    signalform_frame = Frame(notebook, bg=color1)
    notebook.add(signalform_frame, text='Форма')
    signalform_label = None
    signalform_value = ""

    path = os.getcwd() + r"/Images"
    images=[
        PhotoImage(file = path + r"/1-sin.png"),
        PhotoImage(file = path + r"/2-tri.png"),
        PhotoImage(file = path + r"/3-rect.png"),
        PhotoImage(file = path + r"/4-saw.png"),
        ]
    
    temperature_sensor = Sen()

    label_info = tk.Label(root)
    label_info.pack(side=tk.BOTTOM, fill="x")

    params_label_info = tk.Label(root)
    params_label_info.pack(side=tk.BOTTOM, fill="x")

    def __init__(self):
        self.init_all()
        GUI.notebook.pack()
        self.show_info()
        GUI.root.mainloop()

    def signalform_init(self):

        tableWeight=2
        tableHeight=4

        for c in range(tableHeight): GUI.signalform_frame.columnconfigure(index=c, weight=1)
        for r in range(tableWeight): GUI.signalform_frame.rowconfigure(index=r, weight=1)

        signalform_label = Label(GUI.signalform_frame, text="Форма сигнала:", font=25, background=GUI.colors[0], width=100)
        signalform_label.grid(row=0, columnspan=2)

        empty = Label(GUI.signalform_frame, background=GUI.colors[0])
        empty.grid(row=3, columnspan=2)

        counter=0
        for r in range(1, 3):
            for c in range(tableWeight):
                btn = Button(GUI.signalform_frame,image=GUI.images[counter], borderwidth=0, bg=GUI.color2)
                btn.grid(row=r, column=c)
                counter+=1

    def init_all(self):
        self.signalform_init()
        temperature = Classes.TabModel('Тем-ра', 'Температура', GUI.notebook, GUI.colors, Classes.ParamRange(40, 70, 5), "temperature")
        frequency = Classes.TabModel("Час-та", "Частота", GUI.notebook, GUI.colors, Classes.ParamRange(20, 40, 5), "frequency")
        timer = Classes.TabModel("Таймер", "Таймер обратного отсчета", GUI.notebook, GUI.colors, Classes.ParamRange(0, 10, 1), "time")

    #time_label = tk.Label(label_info)
    #time_label.pack(side=tk.RIGHT)
    
    temperature_label = tk.Label(label_info)
    temperature_label.pack(side=tk.RIGHT)

    def show_info(self):
        #current_time = datetime.now().strftime("%H:%M:%S")
        #GUI.time_label.config(text=current_time)
        current_temperature = round(float(GUI.temperature_sensor.get_temperature()),1)
        GUI.temperature_label.config(text=str(current_temperature) + " ℃")
        GUI.temperature_label.after(1000, self.show_info)
