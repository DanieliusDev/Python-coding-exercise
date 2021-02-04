import tkinter as tk


# from tkinter_practice import *


# todo so far everything looks good now time to implement this into my
#  main terminal :)


def username(txt_username):
    if txt_username == "1":
        return True


def password(txt_password):
    if txt_password == "2":
        return True


def ok_button(gotten_username, gotten_password):
    if username(gotten_username) and password(gotten_password):
        print('login success')
        return True
    else:
        print('Incorrect Username or Password')
        return False


root2 = tk.Tk()
root2.title('Login window')
root2.geometry('400x200-550-400')
root2.columnconfigure(0, weight=1)
root2.columnconfigure(1, weight=1)
root2.columnconfigure(2, weight=1)
root2.rowconfigure(0, weight=1)
root2.rowconfigure(1, weight=1)
root2.rowconfigure(2, weight=1)

lbl_username = tk.Label(root2, text='Username')
lbl_username.grid(row=1, column=0)

ent_username = tk.Entry(root2)
ent_username.grid(row=1, column=1)

lbl_password = tk.Label(root2, text='Password')
lbl_password.grid(row=2, column=0, sticky='n')

ent_password = tk.Entry(root2)
ent_password.grid(row=2, column=1, sticky='n')


btn_ok = tk.Button(root2, text='LOGIN', command=lambda: ok_button(ent_username.get(), ent_password.get()), padx=10,
                   pady=5)
btn_ok.grid(row=3, column=1, sticky='nw', )

btn_cancel = tk.Button(root2, text='Cancel', command=quit, padx=10, pady=5)
btn_cancel.grid(row=3, column=1, sticky='n')

root2.mainloop()

