import tkinter as tk


# TODO somehow make password invisible when typing

def login():
    """
    Function which creates login window GUI and asks for credentials
    requires password and login if correct credentials returns True
    otherwise False
    :return: Return True on successful login with correct creds otherwise
    False
    """
    # Initiation of credential input
    validate = False

    # Function meant to test and create username/ID
    def username(txt_username):
        if txt_username == "1":
            return True

    # Function below meant to test and create password
    def password(txt_password):
        if txt_password == "2":
            return True

    def ok_button(gotten_username, gotten_password):
        """
        Takes created username and password from above functions password()
        and username()

        :param gotten_username: username for login as parameter
        :param gotten_password: password for login as parameter
        :return: True if correct credentials else False and login failed
        """
        nonlocal validate
        if username(gotten_username) and password(gotten_password):
            print('login success')
            # below line is variable for returning True on successful credential input
            validate = True
            # after correct credentials below code destroys login GUI
            root2.destroy()
        else:
            lbl_fail = tk.Label(root2, text="Incorrect Username or Password")
            lbl_fail.grid(row=0, column=1, )
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

    btn_ok = tk.Button(root2, text='LOGIN', command=lambda: \
        ok_button(ent_username.get(), ent_password.get()), padx=10, pady=5)

    btn_ok.grid(row=3, column=1, sticky='nw', )

    btn_cancel = tk.Button(root2, text='Cancel', command=quit, padx=10, pady=5)
    btn_cancel.grid(row=3, column=1, sticky='n')

    root2.mainloop()
    return validate
