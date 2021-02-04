import tkinter as tk
from tkinter import *
# from PIL import ImageTk, Image
import webbrowser
import pytz
import datetime
import login_GUI

# from tkinter import messagebox

# Main frame/window
# THIS DOES NOT WORK IF STATEMENT BROKEN ? ? ?
if login_GUI.ok_button(login_GUI.ent_username.get(), login_GUI.ent_password.get()):
    icon = "C:/Users/37060/Downloads/Letter_D_red_35026.ico"

    root = tk.Tk()
    root.title("Main terminal")
    root.geometry("800x600-50-50")
    # Here I get the icon for the left corner of bar on top
    root.iconbitmap(icon)
    new = 1
    url = "https://www.youtube.com"

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)


    # TODO how to get to add, subtract and equal ?


    def calculator_window():
        sec_win = tk.Tk()
        sec_win.title("Calculator")
        lbl2 = tk.Label(sec_win, text="It worked").grid(row=0, column=0)
        sec_win.geometry("320x400")
        sec_win.iconbitmap(icon)
        lbl3 = tk.Label(sec_win, text="")
        lbl3.grid(row=3, column=1)
        # global variable for text input
        global enter_text
        enter_text = tk.Entry(sec_win, width=50, borderwidth=5)
        enter_text.grid(row=0, column=0, columnspan=3)

        # this makes once button clicked from 0-9 to show it in the window
        def button_clicked(args):
            current = enter_text.get()
            enter_text.delete(0, END)
            enter_text.insert(0, current + str(args))

        # clears text from window
        def button_clear():
            enter_text.delete(0, END)

        def button_add():
            first_number = enter_text.get()
            global f_num
            global math
            math = "addition"
            f_num = float(first_number)
            enter_text.delete(0, END)

        def button_subtract():
            first_number = enter_text.get()
            global f_num
            global math
            math = "subtraction"
            f_num = float(first_number)
            enter_text.delete(0, END)

        def button_multiply():
            first_number = enter_text.get()
            global f_num
            global math
            math = "multiply"
            f_num = float(first_number)
            enter_text.delete(0, END)

        def button_division():
            first_number = enter_text.get()
            global f_num
            global math
            math = "division"
            f_num = float(first_number)
            enter_text.delete(0, END)

        def button_equal():
            if math == "addition":
                second_number = enter_text.get()
                enter_text.delete(0, END)
                enter_text.insert(0, f_num + float(second_number))
            if math == "subtraction":
                second_number = enter_text.get()
                enter_text.delete(0, END)
                enter_text.insert(0, f_num - float(second_number))
            if math == "multiply":
                second_number = enter_text.get()
                enter_text.delete(0, END)
                enter_text.insert(0, f_num * float(second_number))
            if math == "division":
                second_number = enter_text.get()
                enter_text.delete(0, END)
                enter_text.insert(0, f_num / float(second_number))

        btn_accept = tk.Button(sec_win, text="Accept", command=button_clicked)

        btn_accept.grid(row=1, column=0)
        btn_accept7 = tk.Button(sec_win, text="7", command=lambda: button_clicked(7), padx=40, pady=5)
        btn_accept8 = tk.Button(sec_win, text="8", command=lambda: button_clicked(8), padx=40, pady=5)
        btn_accept9 = tk.Button(sec_win, text="9", command=lambda: button_clicked(9), padx=40, pady=5)
        btn_accept7.grid(row=2, column=0)
        btn_accept8.grid(row=2, column=1)
        btn_accept9.grid(row=2, column=2)

        btn_accept4 = tk.Button(sec_win, text="4", command=lambda: button_clicked(4), padx=40, pady=5)
        btn_accept5 = tk.Button(sec_win, text="5", command=lambda: button_clicked(5), padx=40, pady=5)
        btn_accept6 = tk.Button(sec_win, text="6", command=lambda: button_clicked(6), padx=40, pady=5)
        btn_accept4.grid(row=3, column=0)
        btn_accept5.grid(row=3, column=1)
        btn_accept6.grid(row=3, column=2)

        btn_accept3 = tk.Button(sec_win, text="3", command=lambda: button_clicked(3), padx=40, pady=5)
        btn_accept2 = tk.Button(sec_win, text="2", command=lambda: button_clicked(2), padx=40, pady=5)
        btn_accept1 = tk.Button(sec_win, text="1", command=lambda: button_clicked(1), padx=40, pady=5)
        btn_accept1.grid(row=4, column=0)
        btn_accept2.grid(row=4, column=1)
        btn_accept3.grid(row=4, column=2)

        btn_plus = tk.Button(sec_win, text="+", command=button_add, padx=40, pady=5)
        btn_minus = tk.Button(sec_win, text="-", command=button_subtract, padx=40, pady=5)
        btn_division = tk.Button(sec_win, text="/", command=button_division, padx=40, pady=5)
        btn_multiplication = tk.Button(sec_win, text="*", command=button_multiply, padx=40, pady=5)
        btn_equal = tk.Button(sec_win, text="=", command=button_equal, padx=38, pady=5)

        btn_plus.grid(row=5, column=0)
        btn_minus.grid(row=5, column=1)
        btn_equal.grid(row=5, column=2)
        btn_multiplication.grid(row=6, column=1)
        btn_division.grid(row=6, column=2)

        btn_clear = tk.Button(sec_win, text="Clear", command=button_clear, padx=31, pady=5)
        btn_clear.grid(row=6, column=0)

        sec_win.mainloop()


    def calorie_counter():
        third_window = tk.Tk()
        third_window.title("Calorie calculator")
        third_window.geometry("400x300")
        third_window.iconbitmap(icon)
        weight_entry = tk.Entry(third_window, width=30, borderwidth=5)
        weight_entry.grid(row=0, column=0, columnspan=2)
        weight_label = tk.Label(third_window, text="Input your weight in KG")
        weight_label.grid(row=0, column=2)
        height_entry = tk.Entry(third_window, width=30, borderwidth=5)
        height_entry.grid(row=1, column=0, columnspan=2)
        height_label = tk.Label(third_window, text="Enter your height in CM")
        height_label.grid(row=1, column=2)
        age_entry = tk.Entry(third_window, width=30, borderwidth=5)
        age_entry.grid(row=2, column=0, columnspan=2)
        age_label = tk.Label(third_window, text="Input your age in YEARS")
        age_label.grid(row=2, column=2)

        r = tk.IntVar(third_window)
        v = IntVar(third_window)

        def activity_button() -> int:
            return r.get()

        def sex_button() -> int:
            return v.get()

        Radiobutton(third_window, text="Lightly active", variable=r, value=1, command=activity_button).grid(
            row=4, column=0)
        Radiobutton(third_window, text="Medium active", variable=r, value=2, command=activity_button).grid(
            row=4, column=1)
        Radiobutton(third_window, text="Heavily active", variable=r, value=3, command=activity_button).grid(
            row=4, column=2)
        Radiobutton(third_window, text="Male", variable=v, value=4, command=sex_button).grid(
            row=5, column=0, padx=25, pady=10)
        Radiobutton(third_window, text="Female", variable=v, value=5, command=sex_button).grid(
            row=5, column=1, padx=25)

        activity_level_1 = 1.2
        activity_level_2 = 1.4
        activity_level_3 = 1.6

        # This func is for getting a 10% reduction in calories for maintenance calories
        def deficit_level_10(calorie_number):
            ten_percent = round(calorie_number / 10)
            calorie_number_deducted = calorie_number - ten_percent
            deficit_label = Label(third_window, text=str(calorie_number) + " - " + str(ten_percent) + " = " + str(
                calorie_number_deducted))
            deficit_label.grid(row=15, column=1)

        def surplus_calorie_10(calorie_number):
            ten_percent = round(calorie_number / 10)
            calorie_number_added = calorie_number + ten_percent
            surplus_label = Label(third_window, text=str(calorie_number) + " - " + str(ten_percent) + " = " + str(
                calorie_number_added))
            surplus_label.grid(row=16, column=1)

        def submit_button():
            if v.get() == 4:
                result = (9.99 * int(weight_entry.get())) + (6.25 * int(height_entry.get())) - (
                        4.92 * int(age_entry.get())) + 5
                if r.get() == 1:
                    result = round(result * activity_level_1)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

                if r.get() == 2:
                    result = round(result * activity_level_2)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

                if r.get() == 3:
                    result = round(result * activity_level_3)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

            if v.get() == 5:
                result = (9.99 * int(weight_entry.get())) + (6.25 * int(height_entry.get())) - (
                        4.92 * int(age_entry.get())) - 161
                if r.get() == 1:
                    result = round(result * activity_level_1)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

                if r.get() == 2:
                    result = round(result * activity_level_2)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

                if r.get() == 3:
                    result = round(result * activity_level_3)
                    result_label = Label(third_window, text=str(result) + " Calories per day").grid(row=14, column=1)
                    deficit_level_10(result)
                    surplus_calorie_10(result)

        btn_submit = tk.Button(third_window, text="Submit", command=submit_button, padx=30, pady=10)
        btn_submit.grid(row=8, column=1)


    def youtube_link():
        webbrowser.open(url, new=new)


    def news_link():
        webbrowser.open("https://www.15min.lt/", new=1)


    def open_file():
        path = open('C:\\Users\\37060\\Test.txt', 'r')
        for line in path:
            print(line)
        path.close()


    # time_canvas = tk.Canvas(root, relief='raised', borderwidth=2, width=250, height=150)
    # time_canvas.grid(row=5, column=1, columnspan=1)

    time_frame = tk.Frame(root, relief='raised', borderwidth=2, width=200, height=200)
    # time_frame.propagate(0)
    time_frame.grid(row=5, column=0, sticky='sew')

    time_result_frame = tk.Frame(root, relief='sunken')
    time_result_frame.grid(row=5, column=1, columnspan=2)

    time_result_lf = tk.LabelFrame(time_result_frame, text="Result")
    time_result_lf.pack()

    time_label = tk.LabelFrame(time_frame, text='Time Zones', padx=30, pady=20, relief='raised')
    time_label.pack()

    ent_time = tk.Entry(time_label, relief='sunken')
    ent_time.pack()

    btn_times = tk.Button(root, text="Timezones", command=quit, pady=5)
    btn_times.grid(row=4, column=2, sticky='ew')


    def world_times():
        choice = ent_time.get()
        while choice != '0':
            # choice = input("Which zone you wanna check:")
            if choice == '0':
                break
            for zone in pytz.all_timezones:
                time_for_zone = pytz.timezone(zone)
                tz_display = datetime.datetime.now(time_for_zone)
                # print("{}".format(zone))
                if choice.lower() in zone.lower():
                    # print("-" * 100)
                    return "{}: {}".format(zone, tz_display)
                    # print("UTC time  \t\t\t\t\t\t\t\t\t{}".format(datetime.datetime.utcnow()))
                    # print("MY Local time is \t\t\t\t\t\t\t{}".format(datetime.datetime.now()))
                    # print("*" * 100)
            else:
                return "No such zone found"


    # result_label = tk.Label(time_frame, text=world_times())
    result_label = tk.Label(time_result_lf, text=world_times())


    def result():
        global result_label
        result_label = tk.Label(time_result_lf, text=world_times())
        result_label.pack()


    def clear_button():
        result_label.destroy()


    btn_accept = tk.Button(time_frame, text='Accept', command=result, padx=20, pady=5)
    btn_accept.pack(side=RIGHT, anchor='ne')

    btn_clear = tk.Button(time_frame, text='Clear', command=clear_button, padx=20, pady=5)
    btn_clear.pack(side=RIGHT, anchor='ne')

    btn_calorie = tk.Button(root, text="Calorie Calculator", command=calorie_counter, padx=20, pady=5)
    btn_calorie.grid(row=3, column=1, sticky='ew')

    btn_youtube = tk.Button(root, text="Youtube", command=youtube_link, padx=40, pady=5)
    btn_youtube.grid(row=3, column=2, sticky='ew')

    btn_excel_search = tk.Button(root, text="Think", command=open_file, padx=35, pady=5)
    btn_excel_search.grid(row=4, column=1, sticky='ew')

    btn_calculator = tk.Button(root, text="Number Calculator", command=calculator_window, padx=21, pady=5)
    btn_calculator.grid(row=3, column=0, sticky='ew')

    btn_15min = tk.Button(root, text="15 Min", command=news_link, padx=53, pady=5)
    btn_15min.grid(row=4, column=0, sticky='ew')
    # here I get the Image on to label of first window
    # first_image = ImageTk.PhotoImage(Image.open("C:/Users/37060/Downloads/comics-batman-logo_97477.png"))
    # label_image = Label(image=first_image)
    # label_image.grid(row=8, column=1)

    root.mainloop()
