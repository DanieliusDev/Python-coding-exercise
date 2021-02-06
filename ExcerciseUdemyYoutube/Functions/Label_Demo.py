import tkinter


# from tkinter import *


# def action_for_start():
#     root = tkinter.Tk()
#     root.title("2nd window")


def new_window_app():
    window = tkinter.Tk()
    window.title("First Window =)")
    window.geometry("400x400")
    greeting = tkinter.Label(text="Hello my friend!!!")
    greeting.pack()
    name = tkinter.Label(text="What's your name ?").pack()
    entry = tkinter.Entry(width="50")
    entry.pack()

    button = tkinter.Button(window, text='stop', width=20, height=2,
                            command=window.destroy)
    button2 = tkinter.Button(window, text='start', width=20, height=2,
                             command=print(entry.get()))
    # print(button)
    # print(button2)
    label = tkinter.Label(window, text="Here you have two buttons")
    label.pack()

    button.pack()
    button2.pack()
    window.mainloop()


new_window_app()
