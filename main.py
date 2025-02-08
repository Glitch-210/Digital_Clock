from tkinter import Tk #used for making window
from tkinter import Label #to write something in the window
import time #to display time

root = Tk()
root.title('Digital Clock')

def present_time():
    # %p = am/pm ,%I = 12hr format,%H= 24Hr format
    # %m = minutes,%s = seconds
    dis_time = time.strftime("%H:%M:%S %p")
    digi_clock.config(text=dis_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("arial",150),bg="Black",fg="white")
digi_clock.pack()

present_time()

root.mainloop()

