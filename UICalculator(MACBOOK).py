from tkinter import *
from tkinter import Tk
from tkmacosx import Button
from tkinter import messagebox

window = Tk()

window.geometry('625x425+10+10')

# Button Function
def insert(function, show):
    if function == "clear":
        textbox.delete(0, 'end') # Clear textbox
    elif function == "delete":
        textbox.delete(textbox.index("end")-1) # Delete last entered
    elif function == "equal":
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
        textbox.insert("end", show) # Enter number/function pressed

# Right Side Buttons (Numbers)
nine = Button(window, command = lambda: insert("nine", "9"), text = "9", fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="blue")
nine.place(x=550,y=50)

eight = Button(window, command = lambda: insert("eight", "8"), text= "8",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
eight.place(x=450,y=50)

seven = Button(window, command = lambda: insert("seven", "7"), text= "7",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
seven.place(x=350,y=50)

six = Button(window, command = lambda: insert("six", "6"), text= "6",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
six.place(x=550,y=150)

five = Button(window, command = lambda: insert("five", "5"), text= "5",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
five.place(x=450,y=150)

four = Button(window, command = lambda: insert("four", "4"), text= "4",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
four.place(x=350,y=150)

three = Button(window, command = lambda: insert("three", "3"), text= "3",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
three.place(x=550,y=250)

two = Button(window, command = lambda: insert("two", "2"), text= "2",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
two.place(x=450,y=250)

one = Button(window, command = lambda: insert("one", "1"), text= "1",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
one.place(x=350,y=250)

delete = Button(window, command = lambda: insert("delete", "⌫"), text= "⌫",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
delete.place(x=550,y=350)

decimal = Button(window, command = lambda: insert("decimal", "."), text= ".",fg = "white", width = 45, height = 45, bg="black", border=5, bordercolor="white")
decimal.place(x=450,y=350)

zero = Button(window, command = lambda: insert("zero", "0"), text= "0", fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
zero.place(x=350,y=350)

# Left Side Buttons (Functions)
plus = Button(window, command = lambda: insert("plus", "+"), text= "+",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
plus.place(x=25,y=250)

subtract = Button(window, command = lambda: insert("subtract", "-"), text= "-",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
subtract.place(x=100,y=250)

multiply = Button(window, command = lambda: insert("multiply", "*"), text= "*",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
multiply.place(x=175,y=250)

divide = Button(window, command = lambda: insert("divide", "/"), text= "/",fg = "white", width = 45, height = 45, bg="black", bordercolor="white", border=5)
divide.place(x=250,y=250)

clear = Button(window, command = lambda: insert("clear", "clear"), text= "Clear",fg = "white", width = 123, height = 47, bg="black", bordercolor="white", border=5)
clear.place(x=25,y=350)

equal = Button(window, command = lambda: insert("equal", "equal"), text= "=",fg = "white", width = 123, height = 47, bg="black", bordercolor="white", border=5)
equal.place(x=175,y=350)

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
