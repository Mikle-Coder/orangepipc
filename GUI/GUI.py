from tkinter.ttk import *
from tkinter import *
import os

 
root = Tk()
root.wm_attributes('-fullscreen','true')
weight = 320
height = 240
#root.geometry(f"{weight}x{height}")
root.configure(bg="#ADADFF")

path = os.getcwd() + r"\Images"

buttonsTable=[]
images=[
   PhotoImage(file = path + r"\1-sin.png"),
   PhotoImage(file = path + r"\2-tri.png"),
   PhotoImage(file = path + r"\3-rect.png"),
   PhotoImage(file = path + r"\4-saw.png"),
]

tableWeight=2
tableHeight=2

for c in range(tableWeight): root.columnconfigure(index=c, weight=1)
for r in range(tableHeight): root.rowconfigure(index=r, weight=1)

counter=0
for r in range(tableHeight):
    for c in range(tableWeight):
        btn = Button(image=images[counter], borderwidth=0, bg='#D8D8FF')
        btn.grid(row=r, column=c)
        counter+=1
 
root.mainloop()