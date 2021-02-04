import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import pytz
import datetime
import login_GUI

user_id = input("id : ")
pwd = input('pwd : ')


if user_id == '1' and pwd == '2':

    root = tk.Tk()
    root.title("Main terminal")
    root.geometry("800x600-50-50")
    # Here I get the icon for the left corner of bar on top
    # root.iconbitmap(icon)
    new = 1
    url = "https://www.youtube.com"

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.mainloop()