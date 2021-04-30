import tkinter as tk
import random
import tkinter.messagebox
from turtle import *

# TODO list:
#  fix issue with last char/letter in underlines as no matter what input in ends game in WON condition how
#  to work around once two words are in as for a guess and there is a space in between? succeeded in concatenating
#  words in case there is more then one, however how to display in GUI the space between words
counter = 6
random_word = ''

# main window for tkinter/gui
root = tk.Tk()
root.title("Hangman")
# opens window in full screen mode
root.attributes('-fullscreen', True)
root.configure(bg='burlywood3')
# configuration for columns so they would stretch
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
# config for rows so they would stretch
root.rowconfigure(0)
root.rowconfigure(1)
root.rowconfigure(2, weight=1)
# game rules displayed in label via 3 columns
games_rules = tk.Label(root, text="\nGuess letters correctly and the guy will live."
                                  "\nMake mistakes and and the guy will be hanged."
                                  "\nAs input you can only provide full word or one letter per time"
                                  "\nDo not use same letters again as it will be counted as mistake"
                                  "\nDo not use combination of letters as it will be counted as mistake"
                                  "\nAfter winning or loosing you can select New game button to restart"
                                  "\nYou will get 6 lives per game, so good luck!", font=30, bg='burlywood3')
games_rules.grid(row=1, column=0, columnspan=3)

# frame for results of game initiated
frame_result_for_word = tk.LabelFrame(root, text="Game result", bg='burlywood2', font=10)
frame_result_for_word.grid(row=2, column=0, sticky='new')


# randomly generated word from list for user to guess
def random_gen_word():
    global random_word, random_theme
    themes_with_list_of_words = {
        'Emotions': ['happy', 'sad', 'angry', 'excited'],
        'Movies': ['avengers', 'geisha', 'interstellar', 'notebook'],
        'Brands': ['gucci', 'adidas', 'nike', 'chanel'],
        'Operating system': ['ios', 'windows', 'linux', 'android'],
        'TV Series': ['lucifer', 'you', 'vikings', 'heist'],
        'Countries': ['united kingdom', 'united states']
    }
    random_theme = random.choice(list(themes_with_list_of_words.keys()))
    themes_list = list(themes_with_list_of_words.get(random_theme))
    random_word = random.choice(list(themes_list))
    print(random_word)
    return random_word


# saving result for func random gen word, otherwise everytime func is called diff word displayed
saved_random_word = random_gen_word().upper()


# changes random word into underlines
def randomly_generated_word_with_underlines():
    underlines = '_ ' * len(remove_whitespace(saved_random_word))
    return underlines


def remove_whitespace(saved_random_word):
    saved_random_word = saved_random_word.replace(" ", "")
    return saved_random_word


# function to display first label with how many letters the word contains
def text_for_label():
    saved_random_word = remove_whitespace(random_word)
    return "Word contains {} letters".format(len(saved_random_word))


underlines = ["_"] * len(saved_random_word)
counter_for_winning = len(underlines) - 1

saved_random_word = remove_whitespace(random_word).upper()


def user_input_for_game(underlines):
    global counter, counter_for_winning
    # to provide underlines instead of selected random word
    user_input = str(entry_input.get()).upper()
    # in case user guesses the word hangman will appear off the hanger and lucky me sign displays
    # or if user guesses word one by one letter
    if user_input == saved_random_word or counter_for_winning <= 0:
        hangman_drawing.speed(8)
        hangman_drawing.clear()
        hangman_drawing.penup()
        hangman_drawing.goto(150, -320)
        hangman_drawing.pendown()
        hangman_drawing.color("Green")
        hangman_drawing.circle(10)
        hangman_drawing.forward(50 * 2)
        hangman_drawing.right(25)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(180)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(115)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(180)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(40)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(130)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.right(180)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.left(70)
        hangman_drawing.forward(40 * 2)
        hangman_drawing.color("Green")
        style = ('Courier', 50, 'italic')
        hangman_drawing.penup()
        hangman_drawing.goto(1, 1)
        hangman_drawing.write("Lucky me!", font=style, align='left')
        disable_submit_entry_widgets()
        winners_message = tk.messagebox.showinfo(title="Winners message", message="Congratulations!"
                                                                                  "\nYou saved the little guy.")

        return f"YOU WON! \nThe word was: {random_word.upper()}"
    # condition for input to be checked if it is IN randomly generated word and letter is not being repeat
    if user_input in saved_random_word and user_input not in underlines:
        # # below for loop will index every letter i = x from the random word
        # # if statement for checking if input was the letter in the word
        for i, x in enumerate(saved_random_word):
            if x == user_input:
                # due to bug where code needs extra click of submit or enter upon filling all the letters correctly
                # here is implemented a counter for winning condition
                counter_for_winning -= 1
                # removes underline once a letter is found in underlines/word and replaces with letter
                underlines[i] = user_input
        return underlines
    else:
        counter -= 1
        if counter == 5:
            hangman_drawing.circle(10)
            return "{} not in the word, tries left: {}".format(user_input, counter)
        elif counter == 4:
            hangman_drawing.forward(50 * 2)
            return "{} not in the word, tries left: {}".format(user_input, counter)
        elif counter == 3:
            hangman_drawing.right(25)
            hangman_drawing.forward(40 * 2)
            return "{} not in the word, tries left: {}".format(user_input, counter)
        elif counter == 2:
            hangman_drawing.right(180)
            hangman_drawing.forward(40 * 2)
            hangman_drawing.right(115)
            hangman_drawing.forward(40 * 2)
            return "{} not in the word, tries left: {}".format(user_input, counter)
        elif counter == 1:
            hangman_drawing.right(180)
            hangman_drawing.forward(40 * 2)
            hangman_drawing.right(40)
            hangman_drawing.forward(40 * 2)
            hangman_drawing.right(130)
            hangman_drawing.forward(40 * 2)
            return "{} not in the word, tries left: {}".format(user_input, counter)
        elif counter == 0:
            hangman_drawing.right(180)
            hangman_drawing.forward(40 * 2)
            hangman_drawing.left(70)
            hangman_drawing.forward(40 * 2)
            hangman_drawing.color("Red")
            style = ('Courier', 30, 'italic')
            hangman_drawing.penup()
            hangman_drawing.goto(100, 10)
            hangman_drawing.write("Dead man hanging...", font=style, align='center')
            loss_message = tkinter.messagebox.showerror(title="Message for loser",
                                                        message="YOU LOST!\nDo better next time.")
            disable_submit_entry_widgets()
            return "{} not in the word, tries left: {}\nYou Lost!".format(user_input, counter)


def submit_button_func(event=None):
    # updates labels frame once submit is being clicked with current input in entry field and removes user input
    user_input = tk.Label(frame_result_for_word, text=user_input_for_game(underlines), font=25, bg='burlywood2')
    user_input.pack()
    entry_input.delete(0, 'end')


# function that returns string upon click of start game which will be users word and input
def start_game_button_func(saved_random_word):
    # Changes name of NEW GAME button to RESET GAME
    button_startgame['text'] = 'Reset game'
    # button_startgame.grid(row=0, column=0, sticky='nsew', )
    # initializing underlines all over again so the letters among underlines would be reset/removed
    global underlines, button_submit, random_theme, counter_for_winning
    underlines = ["_"] * len(saved_random_word)
    counter_for_winning = len(underlines) - 1

    # clears all text within label until very first input for underlines on index 0
    clear_labelframe()

    # initialized counter to keep score of how much attempts available
    global counter
    counter = 6

    # initialize input field for player
    global entry_input
    entry_input = tk.Entry(root, font=25, borderwidth=3, relief='sunken', bg='burlywood1')
    entry_input.grid(row=1, column=0, sticky='new')

    # submit button to accept users input for game
    button_submit = tk.Button(root, text="Submit", command=submit_button_func, bg='burlywood4')
    button_submit.grid(row=1, column=1, sticky='new')

    # game rules label destroyed
    games_rules.destroy()

    # below label for game result with word and letters
    label_displays_underlines = tk.Label(frame_result_for_word,
                                         text=text_for_label() + '\n' + randomly_generated_word_with_underlines(),
                                         font=25, bg='burlywood2')
    label_displays_underlines.pack()

    label_frame_theme_of_words = tk.LabelFrame(root, text='Theme of words', bg='burlywood2', font=10)
    label_frame_theme_of_words.grid(row=2, column=1, sticky='new')

    word_description_label = tk.Label(label_frame_theme_of_words, text=f"\n{random_theme}!", font=25, bg='burlywood2')
    word_description_label.pack()

    global hanger_drawing
    global hangman_drawing
    # initialized canvas for turtles drawing, and putting in into root window
    games_gui_canvas = tk.Canvas(root)
    games_gui_canvas.grid(row=1, column=2, columnspan=2, rowspan=2, sticky='nsew')

    # initializing where turtle will be drawn, in the canvas from above
    screen = TurtleScreen(games_gui_canvas)
    screen.bgcolor('burlywood1')
    # will use turtle instead of arrow for drawing
    hanger_drawing = RawTurtle(screen, shape="turtle")
    hanger_drawing.hideturtle()

    # drawing with pen size 5 for thicker lines
    hanger_drawing.speed(8)
    hanger_drawing.pensize(10)
    # area for hangman to be drawn, the starting point
    hanger_drawing.goto(-100, -500)
    # drawn hangman's signature hanger tower
    hanger_drawing.forward(200)
    hanger_drawing.right(180)
    hanger_drawing.forward(100)
    hanger_drawing.right(90)
    hanger_drawing.forward(500)
    hanger_drawing.right(90)
    hanger_drawing.forward(150)
    hanger_drawing.right(90)
    hanger_drawing.forward(100)
    # begins hangman itself drawing so it could be removed later once upon win
    hangman_drawing = RawTurtle(screen, shape="turtle")
    hangman_drawing.hideturtle()
    hangman_drawing.pencolor('red')
    hangman_drawing.pensize(20)
    hangman_drawing.penup()
    hangman_drawing.goto(150, -100)
    hangman_drawing.pendown()
    hangman_drawing.right(90)


def clear_labelframe():
    # destroy all widgets from frame except first one, that item is skipped which in our case is underlines
    for widget in frame_result_for_word.winfo_children()[0:]:
        widget.destroy()


# lambda used due to function being with parameters and in case we don't want the function to be called
# or launch itself upon opening application lambda prevents from that
button_startgame = tk.Button(root, text='Start game',
                             command=lambda: start_game_button_func(saved_random_word) and changeText, bg='burlywood4')
button_startgame.grid(row=0, column=0, sticky='nsew')


# initialising function for new game button so it would provide new word for game every time it's clicked
# and would update such important variables for losing, winning conditions and reset underlines
def new_game_func():
    # taking global values from other functions
    global underlines, counter_for_winning, saved_random_word
    # everytime new game button clicked providers new word for game
    saved_random_word = remove_whitespace(random_gen_word()).upper()
    start_game_button_func(saved_random_word)
    underlines = ["_"] * len(saved_random_word)
    counter_for_winning = len(underlines) - 1
    return saved_random_word, underlines, counter_for_winning


# as per its name disables submit button and entry window mainly used once game won or lost
def disable_submit_entry_widgets():
    global button_submit, entry_input
    entry_input = tk.Entry(root, font=25, borderwidth=3, relief='sunken', state="disabled")
    entry_input.grid(row=1, column=0, sticky='new')
    if button_submit['state'] == tk.NORMAL:
        button_submit['state'] = tk.DISABLED


def changeText(self):
    return self.text.set("Reset game")


button_new_game = tk.Button(root, text="New game", command=new_game_func, bg='burlywood4')
button_new_game.grid(row=0, column=1, sticky='nsew')

button_exit = tk.Button(root, text='Exit', command=exit, bg='burlywood4')
button_exit.grid(row=0, column=2, sticky='nsew')

# allows to use enter button same way as submit button in GUI
root.bind("<Return>", submit_button_func)

root.mainloop()
