from tkinter import *
from tkinter import messagebox
 
window = Tk()
window.title('Тестовое приложение')
window.geometry('150x80')
window.wm_attributes('-fullscreen','true')

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

textArray = [
   "Привет, Олег",
   "Пока, Олег",
   "Я сказал ПОКА, Олег",
   "Закрыть приложение"
   ]
   
indexOfArray = 0

def calculate_bmi():
   global indexOfArray
   if indexOfArray == len(textArray) - 1:
      window.destroy()
   else:
      indexOfArray = indexOfArray + 1
      cal_btn.configure(text=textArray[indexOfArray])
   
 
cal_btn = Button(
   frame,
   text=textArray[indexOfArray],
   command=calculate_bmi
)

cal_btn.grid(row=5, column=2)
 
window.mainloop()
