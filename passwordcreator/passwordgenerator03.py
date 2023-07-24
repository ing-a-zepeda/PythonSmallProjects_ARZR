#
# Author: Alfonso Zepeda
# Created: 22 - July - 2023
#
# Password Generator GUI
#
# You can choose to add your password: uppercase, lowercase, numbers and/or symbols
# You can choose the lenght of the password
# GUI Added
#
# (c) GPL-3.0 license
#
# Original code from: http://instagram.com/p/Cu3nUuQrKUy
# General TKinter information https://www.tutorialspoint.com/python3/python_gui_programming.htm
# Add Menu: https://www.pythontutorial.net/tkinter/tkinter-menu/
# 


# Random library
import random
# GUI libraries
import tkinter as tk
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import Spinbox
from tkinter import Text

from tkinter import messagebox



# Initialize Window
window = tk.Tk()

# Show About
def showAbout():
    description = "Password Generator GUI \n   Version: 3.0\n   Python Version: 3.11.4\n   Author: Alfonso Zepeda"
    messagebox.showinfo(title="About...", message=description)


# Menu
menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar)

file_menu.add_command(
    label='Exit',
    command=window.destroy,
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

file_menu = Menu(menubar, tearoff=False)


# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)


help_menu.add_command(label='About...', command=showAbout)

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)





# Initialize and add a Label
lbl1 = Label(window, text='Password Generator')
lbl1.pack()

# Initialize and add a Label
lbl2 = Label(window, text='Select Your Characters Desired')
lbl2.pack()

# Creates variables for checkbuttons
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

# Initialize checkbuttons
C1 = Checkbutton(window, text = "Uppercase", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20, )
C2 = Checkbutton(window, text = "Lowercase", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C3 = Checkbutton(window, text = "Number", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)
C4 = Checkbutton(window, text = "Symbol", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 20)

# Adds checkbuttons
C1.pack()
C2.pack()
C3.pack()
C4.pack()

# Initialize and add a Label
lbl3 = Label(window, text='Select Password Lenght')
lbl3.pack()

# Initialize and add a Spinbox
Spbox = Spinbox(window, from_ = 1, to = 20)
Spbox.pack()

# Initialize textbox
text = Text(window, height=2, width= 25)

# Creates a function to generate Password
def generatePassword():
    ''' Function will return the complete string in a textbox

        This function will validate checkbuttons and spinbox to get chars required and lenght for password,
        with this information it will return the complete char collection selected

        Args:
            none

        Returns:
            password(string): if selected it returns the complete char colection if not a message to get checkbuttons marked.
            
    '''
    #Clean textbox
    text.delete('1.0', '25.0')
    
    #Declare variables
    lower = "abcdefghijklmnñopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-!?#$%&="
    all_chars = ""

    # get checkbutton values
    upperCh = int(CheckVar1.get())
    lowerCh = int(CheckVar2.get())
    numbersCh = int(CheckVar3.get())
    symbolCh =  int(CheckVar4.get())

    # Add to all_chars, characters selected
    if(upperCh == 1):
        all_chars += upper
    if(lowerCh == 1):
        all_chars += lower
    if(numbersCh == 1):
        all_chars += numbers
    if(symbolCh == 1):
        all_chars += symbols

    # Get lenght from spinbox
    lenght = int(Spbox.get())

    # Try to generate password, if no checkbutton is marked send a message in textbox
    try:
        password = "".join(random.sample(all_chars, lenght))
    except:
        password = "Choose a checkbox please"

    # Add result to textbox
    text.insert('1.0', password)

# Initialize and add button with generatePassword function attached
btn = Button(window, text='Generate Password', command=generatePassword)
btn.pack()

# Initialize and add label
lbl4 = Label(window, text='Password Generated')
lbl4.pack()

# Add textbox
text.pack()

# Add window configuration
window.title('Password Generator')
window.geometry("300x300")

# Execute
window.mainloop()