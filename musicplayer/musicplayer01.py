# Environment needed:
# To install VirtualEnv we require:
# Open terminal and install with: pip install virtualenv
# once installed go to the project path and type: virtualenv env
# then write on windows: env\Scripts\activate             for linux/mac:  source env\bin\activate
# install pygame 2.5.0: pip install -U pygame==2.5.0
# to deactivate environment just type: deactivate
# to delete environment: rm dir env /s                    for linux/mac: rm -f env

# https://www.instagram.com/p/Cu3mOWyLZDy

# Import libraries

from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

# Creating a window
window = Tk()
window.title('DataFlair Python MP3 Music Player')

# Initialize mixer
mixer.init()

# Create the listbox to contain songs
songs_list=Listbox(window, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Font is defined which is to be used for the button font
defined_font = font.Font(family='Helvetica')

# Play Button
play_button = Button(window, text="Play", width=7, command=Play)
play_button['font']=defined_font
play_button.grid(row = 1, column= 0)

# Pause Button
pause_button = Button(window, text="Pause", widht=7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1, column=1)

mainloop()