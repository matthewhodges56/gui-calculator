# UICalculator.py
# Skyler Emery - Computer Science (Cybersecurity), Jamison Hodges - Computer Science
# GUI Calcultor using tkinter
# Started - 11/15
# Buttons, textbox, and display ready to go - 11/29
# Fixed for windows and one function for button press - 11/30

from tkinter import *
window=Tk() 

# Button Function
def insert(function, show):
    if function == "clear":
        textbox.delete(0, 'end')
    elif function == "delete":
        textbox.delete(textbox.index("end")-1)
    elif function == "equal":
        print("stinky")
    else:
        textbox.insert("end", show)

# Right Side Buttons (Numbers)
nine = Button(window,command=lambda: insert("nine", "9"), text= "9",fg = "white",width = "6", height = "3")
nine.configure(bg = "#19191B")
nine.place(x=550,y=50)

eight = Button(window,command=lambda: insert("eight", "8"), text= "8",fg = "white",width = "6", height = "3")
eight.configure(bg = "#19191B")
eight.place(x=450,y=50)

seven = Button(window,command=lambda: insert("seven", "7"), text= "7",fg = "white",width = "6", height = "3")
seven.configure(bg = "#19191B")
seven.place(x=350,y=50)

six = Button(window,command=lambda: insert("six", "6"), text= "6",fg = "white",width = "6", height = "3")
six.configure(bg = "#19191B")
six.place(x=550,y=150)

five = Button(window,command=lambda: insert("five", "5"), text= "5",fg = "white",width = "6", height = "3")
five.configure(bg = "#19191B")
five.place(x=450,y=150)

four = Button(window,command=lambda: insert("four", "4"), text= "4",fg = "white",width = "6", height = "3")
four.configure(bg = "#19191B")
four.place(x=350,y=150)

three = Button(window,command=lambda: insert("three", "3"), text= "3",fg = "white",width = "6", height = "3")
three.configure(bg = "#19191B")
three.place(x=550,y=250)

two = Button(window,command=lambda: insert("two", "2"), text= "2",fg = "white",width = "6", height = "3")
two.configure(bg = "#19191B")
two.place(x=450,y=250)

one = Button(window,command=lambda: insert("one", "1"), text= "1",fg = "white",width = "6", height = "3")
one.configure(bg = "#19191B")
one.place(x=350,y=250)

delete = Button(window,command=lambda: insert("delete", "⌫"), text= "⌫",fg = "white",width = "6", height = "3")
delete.configure(bg = "#19191B")
delete.place(x=550,y=350)

decimal = Button(window,command=lambda: insert("decimal", "."), text= ".",fg = "white",width = "6", height = "3")
decimal.configure(bg = "#19191B")
decimal.place(x=450,y=350)

zero = Button(window,command=lambda: insert("zero", "0"), text= "0",fg = "white", width = "6", height = "3")
zero.configure(bg = "#19191B")
zero.place(x=350,y=350)

# Left Side Buttons (Functions)
plus = Button(window,command=lambda: insert("plus", " + "), text= "+",fg = "white",width = "6", height = "3")
plus.configure(bg="#7D7D7D")
plus.place(x=25,y=150)

subtract = Button(window,command=lambda: insert("subtract", " - "), text= "-",fg = "white",width = "6", height = "3")
subtract.configure(bg="#7D7D7D")
subtract.place(x=100,y=150)

multiply = Button(window,command=lambda: insert("multiply", " x "), text= "x",fg = "white",width = "6", height = "3")
multiply.configure(bg="#7D7D7D")
multiply.place(x=175,y=150)

divide = Button(window,command=lambda: insert("divide", " ÷ "), text= "÷",fg = "white",width = "6", height = "3")
divide.configure(bg="#7D7D7D")
divide.place(x=250,y=150)

exponent = Button(window,command=lambda: insert("exponent", "x²"), text= "x²",width = "6", height = "3")
exponent.configure(bg="#BDBBBE")
exponent.place(x=25,y=250)

percent = Button(window,command=lambda: insert("percent", " % "), text= "%",width = "6", height = "3")
percent.configure(bg="#BDBBBE")
percent.place(x=100,y=250)

pi = Button(window,command=lambda: insert("pi", "π"), text= "π",width = "6", height = "3")
pi.configure(bg="#BDBBBE")
pi.place(x=175,y=250)

sqr = Button(window,command=lambda: insert("sqr", "√"), text= "√",width = "6", height = "3")
sqr.configure(bg="#BDBBBE")
sqr.place(x=250,y=250)

clear = Button(window,command=lambda: insert("clear", "Clear"), text= "Clear",fg = "white", width = "17",height = "3" )
clear.configure(bg = "#6EAF41")
clear.place(x=25,y=350)

equal = Button(window, command = lambda: insert("equal", "equal"), text= "=",fg = "white",width = "17",height = "3" )
equal.configure(bg="#7D7D7D")
equal.place(x=175,y=350)

# Texbox
textbox = Entry(window,width = "18",font = ("Ariel 20"))
textbox.place(x=26,y=60)

# Background Display
window.geometry("625x425+10+10")
window.configure(bg="#53585B")
window.title("Calculator")
window.resizable(False, False)
window.mainloop()