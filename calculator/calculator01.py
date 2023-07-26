#
# Author: Alfonso Zepeda
# Created: 25 - July - 2023
#
# Calculator GUI
#
# Simple calculator
#
# (c) GPL-3.0 license
#
# Original code from: http://instagram.com/p/Cu1Hi4HLAaK  - CodeWithHarry
# Bind: https://www.pythontutorial.net/tkinter/tkinter-event-binding/
# 

keyfont = "lucida 15 bold"

from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.geometry("300x315")
root.title("Calculator")

temporalresult = 0
screenstr = ""
screenvalue = StringVar()
screenvalue.set("")
screen = Entry(root, justify="right", textvar=screenvalue, font="lucida 35 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")

def clearBtn():
    global screenstr
    screenstr=""
    global temporalresult 
    temporalresult = 0
    global screenvalue
    screenvalue.set(screenstr)


b = Button(f, text="C", height=1, width=5, font=keyfont, command = clearBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind('<Return>', click)

b = Button(f, text="√",  height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="^",  height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="%",  height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

f.pack()


f = Frame(root, bg="grey")


def sevenBtn():
    global screenvalue
    global screenstr

    screenstr += "7"
    screenvalue.set(screenstr)
    
b = Button(f, text="7", height=1, width=5, font=keyfont, command =sevenBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def eightBtn():
    global screenvalue
    global screenstr

    screenstr += "8"
    screenvalue.set(screenstr)

b = Button(f, text="8", height=1, width=5, font=keyfont, command = eightBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def nineBtn():
    global screenvalue
    global screenstr

    screenstr += "9"
    screenvalue.set(screenstr)

b = Button(f, text="9", height=1, width=5, font=keyfont, command=nineBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="+", height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

f.pack()


f = Frame(root, bg="grey")

def fourBtn():
    global screenvalue
    global screenstr

    screenstr += "4"
    screenvalue.set(screenstr)

b = Button(f, text="4", height=1, width=5, font=keyfont, command= fourBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def fiveBtn():
    global screenvalue
    global screenstr

    screenstr += "5"
    screenvalue.set(screenstr)

b = Button(f, text="5", height=1, width=5, font=keyfont, command=fiveBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def sixBtn():
    global screenvalue
    global screenstr

    screenstr += "6"
    screenvalue.set(screenstr)

b = Button(f, text="6", height=1, width=5, font=keyfont, command=sixBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="-", height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

f.pack()


f = Frame(root, bg="grey")

def oneBtn():
    global screenvalue
    global screenstr

    screenstr += "1"
    screenvalue.set(screenstr)

b = Button(f, text="1", height=1, width=5, font=keyfont, command=oneBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def twoBtn():
    global screenvalue
    global screenstr

    screenstr += "2"
    screenvalue.set(screenstr)

b = Button(f, text="2", height=1, width=5, font=keyfont, command=twoBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def threeBtn():
    global screenvalue
    global screenstr

    screenstr += "3"
    screenvalue.set(screenstr)

b = Button(f, text="3", height=1, width=5, font=keyfont, command=threeBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="*", height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

f.pack()


f = Frame(root, bg="grey")

def zeroBtn():
    global screenvalue
    global screenstr

    screenstr += "0"
    screenvalue.set(screenstr)

b = Button(f, text="0", height=1, width=5, font=keyfont, command=zeroBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

def dotBtn():
    global screenvalue
    global screenstr

    screenstr += "."
    screenvalue.set(screenstr)
b = Button(f, text=".", height=1, width=5, font=keyfont, command=dotBtn)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="=", background='#ff8000',height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)

b = Button(f, text="/", height=1, width=5, font=keyfont)
b.pack(side=LEFT, ipadx=1, ipady=1, padx=1, pady=1)
#b.bind("", click)
f.pack()

root.mainloop()