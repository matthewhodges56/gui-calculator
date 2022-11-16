#UICalculator.py
#Skyler Emery - Computer Science (Cybersecurity)
#11/15/22
#This is a calculator to do maf with

from tkinter import *
window=Tk() 

#--------------------------------------------------------RIGHT SIDE

nine = Button(window, text= "9",fg = "white",width = "2", height = "2")
nine.configure(bg = "#19191B")
nine.place(x=550,y=50)

eight = Button(window, text= "8",fg = "white",width = "2", height = "2")
eight.configure(bg = "#19191B")
eight.place(x=450,y=50)

seven = Button(window, text= "7",fg = "white",width = "2", height = "2")
seven.configure(bg = "#19191B")
seven.place(x=350,y=50)

six = Button(window, text= "6",fg = "white",width = "2", height = "2")
six.configure(bg = "#19191B")
six.place(x=550,y=150)

five = Button(window, text= "5",fg = "white",width = "2", height = "2")
five.configure(bg = "#19191B")
five.place(x=450,y=150)

four = Button(window, text= "4",fg = "white",width = "2", height = "2")
four.configure(bg = "#19191B")
four.place(x=350,y=150)

three = Button(window, text= "3",fg = "white",width = "2", height = "2")
three.configure(bg = "#19191B")
three.place(x=550,y=250)

two = Button(window, text= "2",fg = "white",width = "2", height = "2")
two.configure(bg = "#19191B")
two.place(x=450,y=250)

one = Button(window, text= "1",fg = "white",width = "2", height = "2")
one.configure(bg = "#19191B")
one.place(x=350,y=250)

delete = Button(window, text= "delete",fg = "white",width = "2", height = "2")
delete.configure(bg = "#19191B")
delete.place(x=550,y=350)

decimal = Button(window, text= ".",fg = "white",width = "2", height = "2")
decimal.configure(bg = "#19191B")
decimal.place(x=450,y=350)

zero = Button(window, text= "0",fg = "white", width = "2", height = "2")
zero.configure(bg = "#19191B")
zero.place(x=350,y=350)

#------------------------------------------------------------------LEFT SIDE

plus = Button(window, text= "+",fg = "white",width = "2", height = "2")
plus.configure(bg="#7D7D7D")
plus.place(x=25,y=150)

subtract = Button(window, text= "-",fg = "white",width = "2", height = "2")
subtract.configure(bg="#7D7D7D")
subtract.place(x=100,y=150)

multiply = Button(window, text= "x",fg = "white",width = "2", height = "2")
multiply.configure(bg="#7D7D7D")
multiply.place(x=175,y=150)

divide = Button(window, text= "÷",fg = "white",width = "2", height = "2")
divide.configure(bg="#7D7D7D")
divide.place(x=250,y=150)

exponent = Button(window, text= "*",width = "2", height = "2")
exponent.configure(bg="#BDBBBE")
exponent.place(x=25,y=250)

percent = Button(window, text= "%",width = "2", height = "2")
percent.configure(bg="#BDBBBE")
percent.place(x=100,y=250)

pi = Button(window, text= "π",width = "2", height = "2")
pi.configure(bg="#BDBBBE")
pi.place(x=175,y=250)

para = Button(window, text= "()",width = "2", height = "2")
para.configure(bg="#BDBBBE")
para.place(x=250,y=250)

clear = Button(window, text= "Clear",fg = "white", width = "12",height = "2" )
clear.configure(bg = "#6EAF41")
clear.place(x=25,y=350)

equal = Button(window, text= "=",fg = "white",width = "12",height = "2" )
equal.configure(bg="#7D7D7D")
equal.place(x=175,y=350)

#BACKGROUND
window.geometry("625x425+10+10")
window.configure(bg="#53585B")
window.title("Calculator")
window.resizable(False, False)
window.mainloop()