from tkinter.ttk import *
from tkinter import *
import os

color1='#ADADFF'
color2='#D8D8FF'
 
root = Tk()
root.configure(bg=color1)
weight = 320
height = 240
root.geometry(f"{weight}x{height}")

#root.wm_attributes('-fullscreen','true')

style = Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')
notebook = Notebook(root, style='lefttab.TNotebook', width=weight-55, height=height)


#________________________________________________________Форма сигнала_______________________________________________________________________

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

#_________________________________________________________Температура_______________________________________________________________________

temperature_frame = Frame(notebook,bg=color1)
notebook.add(temperature_frame, text='Тем-ра')
temperature_label = None
temperature_value = 0


def temperature_init():

    tableWeight=2
    tableHeight=3

    for c in range(tableHeight): temperature_frame.columnconfigure(index=c, weight=1)
    for r in range(tableWeight): temperature_frame.rowconfigure(index=r, weight=1)

    label = Label(temperature_frame, text="Температура:", font=25, background=color1, width=100)
    label.grid(row=0,columnspan=2,sticky=S)

    temperature_label = Label(temperature_frame, text=temperature_value, background=color1, font=25)
    temperature_label.grid(row=1, columnspan=2,sticky=S)

    control = Control(temperature_frame, temperature_value, temperature_label)


#___________________________________________________________Частота_______________________________________________________________________
frequency_frame = Frame(notebook,bg=color1)
notebook.add(frequency_frame, text='Час-та')
frequency_label = None
frequency_value = 0

def frequency_init():

    tableWeight=2
    tableHeight=3
    
    for c in range(tableHeight): frequency_frame.columnconfigure(index=c, weight=1)
    for r in range(tableWeight): frequency_frame.rowconfigure(index=r, weight=1)

    label = Label(frequency_frame, text="Частота:", font=25, background=color1, width=100)
    label.grid(row=0,columnspan=2,sticky=S)

    frequency_label = Label(frequency_frame, text=frequency_value, background=color1, font=25)
    frequency_label.grid(row=1, columnspan=2,sticky=S)

    control = Control(frequency_frame, frequency_value, frequency_label)


#___________________________________________________________Таймер_______________________________________________________________________

timer_frame = Frame(notebook,bg=color1)
notebook.add(timer_frame, text='Время')

#___________________________________________________________Контроль цифрами_______________________________________________________________________

class Control:

    def __init__(self, frame, value, label):
        self.holding_trigger = False
        self.running = False
        self.jobid = None

        self.frame = frame
        self.value = value
        self.label = label

        direction = ["+", "-"]
        for n in range(len(direction)):
            button = Button(self.frame, text=direction[n], font=25, bg=color2, borderwidth=0, width=10)
            button.grid(row=2, column=n, pady= 50,sticky=N)
            button.bind('<ButtonPress-1>', lambda event, direction=direction[n]: self.start_motor(direction))
            button.bind('<ButtonRelease-1>', lambda event: self.stop_motor())

    def start_motor(self, direction):
        self.move(direction)

    def stop_motor(self):
        self.frame.after_cancel(self.jobid)
        self.holding_trigger=False

    def move(self, direction):
        if(direction=="+"):
            self.value += 1
        else:
            self.value -= 1
        self.label.configure(text=self.value)

        time = 500
        if(self.holding_trigger==True):
            time=50
        else:
            self.holding_trigger=True

        self.jobid = root.after(time,  self.move, direction)
    

signalform_init()
temperature_init()
frequency_init()


notebook.pack()
root.mainloop()
