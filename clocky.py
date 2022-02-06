from tkinter import *

from time import strftime
from tkinter.font import Font

root = Tk()#display root window
root.title("Clocky")

def time1():
    strin1 = strftime("%I:%M:%S %p")#12 hr-format, p - PM/AM
    label.config(text= strin1)
    label.after(1000, time1) #1 sec

def time2():
    strin2 = strftime("%H:%M:%S %p")#12 hr-format, p - PM/AM
    label2.config(text= strin2)
    label2.after(1000, time2) #1 sec
    
    
label = Label(root, font = ("ds-digital", 50, "bold"), bg = "black", fg = "orange")
label.pack(anchor = 'center')

label2 = Label(root, font = ("DS-Digital", 50, "bold"), bg = "black", fg = "turquoise")
label2.pack(anchor = 'center')
time1()
time2()
mainloop() #to run the application