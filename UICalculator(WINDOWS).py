# UICalculator.py
# Skyler Emery - Computer Science (Cybersecurity), Jamison Hodges - Computer Science
# GUI Calcultor using tkinter
# Started - 11/15
# Buttons, textbox, and display ready to go - 11/29
# Fixed for windows and one function for button press - 11/30
# Finished evaluating problems and catching errors with feedback, also added label - 12/1

from tkinter import *
from tkinter import messagebox
window = Tk() 

# Button Function
def buttonPress(function):
    if function == "clear":
        textbox.delete(0, 'end') # Clear textbox
    elif function == "delete":
        textbox.delete(textbox.index("end")-1) # Delete last entered
    elif function == "equals":
        expression = textbox.get() # Get current value of textbox
        try:
            value = eval(expression) # Evaluate the math problem
            messagebox.showinfo("Answer", "Answer = " + str(value)) # Popup window with answer
        except NameError: # Catch any name errors
            messagebox.showerror("Error", "Only numbers and available functions are allowed!")
        except ZeroDivisionError: # Catch any divide/multiply by 0 erros
            messagebox.showinfo("Answer", "Answer = 0")
        textbox.delete(0, 'end') # Clear textbox after problem
    else:
        textbox.insert("end", function) # Enter number/function pressed

# Right Side Buttons (Numbers)
nine = Button(window,command=lambda: buttonPress("9"), text = "9", fg = "white", width = "6", height = "3")
nine.configure(bg = "#19191B")
nine.place(x=550,y=50)

eight = Button(window,command=lambda: buttonPress("8"), text = "8", fg = "white", width = "6", height = "3")
eight.configure(bg = "#19191B")
eight.place(x=450,y=50)

seven = Button(window,command=lambda: buttonPress("7"), text = "7", fg = "white", width = "6", height = "3")
seven.configure(bg = "#19191B")
seven.place(x=350,y=50)

six = Button(window,command=lambda: buttonPress("6"), text = "6", fg = "white", width = "6", height = "3")
six.configure(bg = "#19191B")
six.place(x=550,y=150)

five = Button(window,command=lambda: buttonPress("5"), text= "5", fg = "white", width = "6", height = "3")
five.configure(bg = "#19191B")
five.place(x=450,y=150)

four = Button(window,command=lambda: buttonPress("4"), text = "4", fg = "white", width = "6", height = "3")
four.configure(bg = "#19191B")
four.place(x=350,y=150)

three = Button(window,command=lambda: buttonPress("3"), text = "3", fg = "white", width = "6", height = "3")
three.configure(bg = "#19191B")
three.place(x=550,y=250)

two = Button(window,command=lambda: buttonPress("2"), text = "2", fg = "white", width = "6", height = "3")
two.configure(bg = "#19191B")
two.place(x=450,y=250)

one = Button(window,command=lambda: buttonPress("1"), text = "1", fg = "white", width = "6", height = "3")
one.configure(bg = "#19191B")
one.place(x=350,y=250)

delete = Button(window,command=lambda: buttonPress("delete"), text= "⌫", fg = "white", width = "6", height = "3")
delete.configure(bg = "#19191B")
delete.place(x=550,y=350)

decimal = Button(window,command=lambda: buttonPress("."), text = ".", fg = "white", width = "6", height = "3")
decimal.configure(bg = "#19191B")
decimal.place(x=450,y=350)

zero = Button(window,command=lambda: buttonPress("0"), text = "0", fg = "white", width = "6", height = "3")
zero.configure(bg = "#19191B")
zero.place(x=350,y=350)

# Left Side Buttons (Functions)
plus = Button(window,command=lambda: buttonPress("+"), text = "+", fg = "white", width = "6", height = "3")
plus.configure(bg="#7D7D7D")
plus.place(x=25,y=250)

subtract = Button(window,command=lambda: buttonPress("-"), text = "-", fg = "white", width = "6", height = "3")
subtract.configure(bg="#7D7D7D")
subtract.place(x=100,y=250)

multiply = Button(window,command=lambda: buttonPress("*"), text= "*", fg = "white", width = "6", height = "3")
multiply.configure(bg="#7D7D7D")
multiply.place(x=175,y=250)

divide = Button(window,command=lambda: buttonPress("/"), text = "/", fg = "white", width = "6", height = "3")
divide.configure(bg="#7D7D7D")
divide.place(x=250,y=250)

clear = Button(window,command=lambda: buttonPress("clear"), text = "Clear", fg = "white", width = "17", height = "3" )
clear.configure(bg = "#6EAF41")
clear.place(x=25,y=350)

equals = Button(window, command = lambda: buttonPress("equals"), text = "=", fg = "white", width = "17", height = "3" )
equals.configure(bg="#7D7D7D")
equals.place(x=175,y=350)

# Texbox
textbox = Entry(window, width = "8", font = ("Arial 47"))
textbox.place(x = 21, y = 125)

# Label
label = Label(window, bg = "#53585B", text = "Simple Calculator", font = ("Arial 25"))
label.place(x = 35, y = 55)

# Background Display
window.geometry("625x425+10+10")
window.configure(bg="#53585B")
window.title("Calculator")
window.resizable(False, False)
window.mainloop()
