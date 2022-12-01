from tkinter import *
from tkinter import Tk
from tkmacosx import Button

window = Tk()

window.geometry('625x425+10+10')

def nine():
    textbox.insert("end", "9")

def eight():
    textbox.insert(1, "8")

def seven():
    textbox.insert(1, "7")

def six():
    textbox.insert(1, "6")

def five():
    textbox.insert(1, "5")

def four():
    textbox.insert(1, "4")

def three():
    textbox.insert(1, "3")

def two():
    textbox.insert(1, "2")

def one():
    textbox.insert(1, "1")

def zero():
    textbox.insert(1, "0")

def clear():
    textbox.delete(0, 'end')

nine = Button(window, command = nine, text = "9", fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="blue")
nine.place(x=550,y=50)

eight = Button(window, command = eight, text= "8",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
eight.place(x=450,y=50)

seven = Button(window, command = seven, text= "7",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
seven.place(x=350,y=50)

six = Button(window, command = six, text= "6",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
six.place(x=550,y=150)

five = Button(window, command = five, text= "5",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
five.place(x=450,y=150)

four = Button(window, command = four, text= "4",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
four.place(x=350,y=150)

three = Button(window, command = three, text= "3",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
three.place(x=550,y=250)

two = Button(window, command = two, text= "2",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
two.place(x=450,y=250)

one = Button(window, command = one, text= "1",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
one.place(x=350,y=250)

delete = Button(window, text= "Del",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
delete.place(x=550,y=350)

decimal = Button(window, text= ".",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
decimal.place(x=450,y=350)

zero = Button(window, command = zero, text= "0", fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
zero.place(x=350,y=350)

plus = Button(window, text= "+",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
plus.place(x=25,y=150)

subtract = Button(window, text= "-",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
subtract.place(x=100,y=150)

multiply = Button(window, text= "x",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
multiply.place(x=175,y=150)

divide = Button(window, text= "÷",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
divide.place(x=250,y=150)

exponent = Button(window, text= "*",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
exponent.place(x=25,y=250)

percent = Button(window, text= "%",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
percent.place(x=100,y=250)

pi = Button(window, text= "π",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
pi.place(x=175,y=250)

para = Button(window, text= "()",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
para.place(x=250,y=250)

clear = Button(window, command = clear, text= "Clear",fg = "white", width = 123, height = 47, bg="black", bordercolor="white", border=5)
clear.place(x=25,y=350)

equal = Button(window, text= "=",fg = "white", width = 123, height = 47, bg="black", bordercolor="white", border=5)
equal.place(x=175,y=350)

textbox = Entry(window, width = 20, font = ("Ariel 20"))
textbox.place(x=21,y=55)

window.configure(bg="#53585B")
window.title("Calculator")
window.resizable(False, False)
window.mainloop()
