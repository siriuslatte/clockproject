# Imports
from tkinter import *
from tkinter.ttk import *

from time import strftime
from googletrans import Translator

import ctypes
import locale

# Variables declaration
master = Tk()
timeLabel = Label(
    master,
    font=("Helvetica", 25),
    foreground="black"
)
dayLabel = Label(
    master,
    font=("Helvetica", 10),
    foreground="black"
)

translator = Translator()

# Region identifier for the language translation
windll = ctypes.windll.kernel32
regionLanguage = locale.windows_locale[windll.GetUserDefaultUILanguage()]

# Configuration
master.title("Clock Application")
master.resizable(width=False, height=False)  # It can't be resized
master.geometry("300x65")
master.iconphoto(False, PhotoImage(file="./resources/clockimage.png"))

dayLabel.pack(anchor="center")
timeLabel.pack(anchor="center")


# Functions
def time():
    currentTime = strftime("%X %p").lower()

    # Translation available
    stringVanilla = strftime("%A, %d of %B").lower()
    result = translator.translate(stringVanilla, src="en", dest=regionLanguage)
    currentDay = result.text

    timeLabel.config(text=currentTime)
    dayLabel.config(text=currentDay)

    # The function gets invoked every second (or 1000 milliseconds) and updates the text again
    timeLabel.after(100, time)
    dayLabel.after(86400000, time)  # Milliseconds required for a day


# Initializer
time()
mainloop()
