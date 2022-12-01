from tkinter import *
from tkinter import Tk
from tkmacosx import Button
from tkinter import messagebox

window = Tk()

window.geometry('625x425+10+10')

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
nine = Button(window, command = lambda: buttonPress("9"), text = "9", fg = "white", width = 45, height = 45, bg = "black", border = 5)
nine.place(x=550,y=50)

eight = Button(window, command = lambda: buttonPress("8"), text = "8", fg = "white", width = 45, height = 45, bg = "black", border = 5 )
eight.place(x=450,y=50)

seven = Button(window, command = lambda: buttonPress("7"), text = "7", fg = "white", width = 45, height = 45, bg = "black", border = 5)
seven.place(x=350,y=50)

six = Button(window, command = lambda: buttonPress("6"), text = "6", fg = "white", width = 45, height = 45, bg = "black", border = 5)
six.place(x=550,y=150)

five = Button(window, command = lambda: buttonPress("5"), text = "5", fg = "white", width = 45, height = 45, bg = "black", border = 5)
five.place(x=450,y=150)

four = Button(window, command = lambda: buttonPress("4"), text = "4",fg = "white", width = 45, height = 45, bg = "black", border = 5)
four.place(x=350,y=150)

three = Button(window, command = lambda: buttonPress("3"), text = "3", fg = "white", width = 45, height = 45, bg = "black", border = 5)
three.place(x=550,y=250)

two = Button(window, command = lambda: buttonPress("2"), text = "2", fg = "white", width = 45, height = 45, bg = "black", border = 5)
two.place(x=450,y=250)

one = Button(window, command = lambda: buttonPress("1"), text = "1", fg = "white", width = 45, height = 45, bg = "black", border = 5)
one.place(x=350,y=250)

delete = Button(window, command = lambda: buttonPress("delete"), text = "⌫", fg = "white", width = 45, height = 45, bg = "black", border = 5)
delete.place(x=550,y=350)

decimal = Button(window, command = lambda: buttonPress("."), text = ".", fg = "white", width = 45, height = 45, bg = "black", border = 5)
decimal.place(x=450,y=350)

zero = Button(window, command = lambda: buttonPress("0"), text = "0", fg = "white", width = 45, height = 45, bg = "black", border = 5)
zero.place(x=350,y=350)

# Left Side Buttons (Functions)
plus = Button(window, command = lambda: buttonPress("+"), text = "+", fg = "white", width = 45, height = 45, bg = "black", border = 5)
plus.place(x=25,y=250)

subtract = Button(window, command = lambda: buttonPress("-"), text = "-", fg = "white", width = 45, height = 45, bg = "black", border = 5)
subtract.place(x=100,y=250)

multiply = Button(window, command = lambda: buttonPress("*"), text = "*", fg = "white", width = 45, height = 45, bg = "black", border = 5)
multiply.place(x=175,y=250)

divide = Button(window, command = lambda: buttonPress("/"), text = "/", fg = "white", width = 45, height = 45, bg = "black", border = 5)
divide.place(x=250,y=250)

clear = Button(window, command = lambda: buttonPress("clear"), text = "Clear", fg = "white", width = 123, height = 47, bg = "black", border = 5)
clear.place(x=25,y=350)

equals = Button(window, command = lambda: buttonPress("equals"), text = "=", fg = "white", width = 123, height = 47, bg = "black", border = 5)
equals.place(x=175,y=350)

# Textbox
textbox = Entry(window, width = 8, font = ("Arial 60"))
textbox.place(x=22,y=125)

# Label
label = Label(window, bg = "#53585B", text = "Simple Calculator", font = ("Arial 30"))
label.place(x = 43, y = 55)

# Display Configurations
window.configure(bg="#53585B")
window.title("Calculator")
window.resizable(False, False)
window.mainloop()
