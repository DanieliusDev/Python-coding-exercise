from tkinter import *
import tkinter


def window_with_choice():
    master = Tk()
    var1 = IntVar()
    Checkbutton(master, text='Daniel', variable=var1).grid(row=2, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text='Vilte', variable=var2).grid(row=1, sticky=W)

    mainloop()


window_with_choice()
