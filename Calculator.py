#Program to design a simple Calculator using GUI Tkinter

#importing required module
from functools import partial
from tkinter import *

#Defining global variable for calculation
calc_euation=""

##Define various command functions
#function when a Button is pressed
def press_but(key):
    global calc_euation
    calc_euation = calc_euation+str(key)
    input.set(calc_euation)

#function of clear button
def clr():
    global calc_euation
    calc_euation = ""
    input.set(calc_euation)

#function for Equal button
def equal():
    global calc_euation
    output = eval(calc_euation)
    input.set(output)

#creating GUI using Tkinter
win=Tk()
win.title("Calculator")
win.geometry("350x350")

#tkinter variable for entry box
input = StringVar()

#creating entry box at zeroth row
entry_box = Entry(win,textvariable=input,width=35,font="30",bg="grey",fg="black")
entry_box.grid(columnspan=10,ipady=15,padx=5)

#creating buttons for first row
but7 = Button(win,text="7",height=4,command=partial(press_but,7),width=7,bg="black",fg="white")
but7.grid(row=1,column=0)
but8 = Button(win,text="8",height=4,command=lambda:press_but(8),width=7,bg="black",fg="white")
but8.grid(row=1,column=1)
but9 = Button(win,text="9",height=4,command=lambda:press_but(9),width=7,bg="black",fg="white")
but9.grid(row=1,column=2)
butclr = Button(win,text="Clear",height=4,command=lambda:clr(),width=7,bg="red",fg="black")
butclr.grid(row=1,column=3)
butmul = Button(win,text="X",height=4,command=lambda:press_but("*"),width=7,bg="black",fg="white")
butmul.grid(row=1,column=4)

#creating buttons for second row
but4 = Button(win,text="4",height=4,command=lambda:press_but(4),width=7,bg="black",fg="white")
but4.grid(row=2,column=0)
but5 = Button(win,text="5",height=4,command=lambda:press_but(5),width=7,bg="black",fg="white")
but5.grid(row=2,column=1)
but6 = Button(win,text="6",height=4,command=lambda:press_but(6),width=7,bg="black",fg="white")
but6.grid(row=2,column=2)
butmod = Button(win,text="%",height=4,command=lambda:press_but("%"),width=7,bg="black",fg="white")
butmod.grid(row=2,column=3)
butdiv = Button(win,text="/",height=4,command=lambda:press_but("/"),width=7,bg="black",fg="white")
butdiv.grid(row=2,column=4)

#creating buttons for third row
but1 = Button(win,text="1",height=4,command=lambda:press_but(1),width=7,bg="black",fg="white")
but1.grid(row=3,column=0)
but2 = Button(win,text="2",height=4,command=lambda:press_but(2),width=7,bg="black",fg="white")
but2.grid(row=3,column=1)
but3 = Button(win,text="3",height=4,command=lambda:press_but(3),width=7,bg="black",fg="white")
but3.grid(row=3,column=2)
butdot = Button(win,text=".",height=4,command=lambda:press_but("."),width=7,bg="black",fg="white")
butdot.grid(row=3,column=3)
butplus = Button(win,text="+",height=4,command=lambda:press_but("+"),width=7,bg="black",fg="white")
butplus.grid(row=3,column=4)

#creating buttons for fourth row
but0 = Button(win,text="0",height=4,command=lambda:press_but(0),width=7,bg="black",fg="white")
but0.grid(row=4,column=0)
butpow = Button(win,text="x^2",height=4,command=lambda:press_but("**"),width=7,bg="black",fg="white")
butpow.grid(row=4,column=1)
butequal = Button(win,text="=",height=4,command=lambda:equal(),width=7,bg="black",fg="white")
butequal.grid(row=4,column=3)
butmin = Button(win,text="-",height=4,command=lambda:press_but("-"),width=7,bg="black",fg="white")
butmin.grid(row=4,column=4)
butroot = Button(win,text="(x)^1/2",height=4,command=lambda:press_but("**1/2"),width=7,bg="black",fg="white")
butroot.grid(row=4,column=2)

#to run self indifinte loop
win.mainloop()

#program finished

