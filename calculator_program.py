from tkinter import *  # Import all classes and functions from the tkinter module

def button_press(num):
    global equation_text  # Use the global equation_text variable
    equation_text = equation_text + str(num)  # Append the pressed button's value to the equation
    equation_label.set(equation_text)  # Update the label to show the current equation

def equals():
    global equation_text  # Access the global equation_text
    try:
        total = str(eval(equation_text))  # Evaluate the expression and convert the result to string
        equation_label.set(total)  # Display the result
        equation_text = total  # Store result as new equation for continued calculation
    except SyntaxError:  # Handle invalid expressions
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:  # Handle division by zero
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text  # Access the global equation_text
    equation_label.set("")  # Clear the label
    equation_text = ""  # Reset the equation

# Create the main window
window = Tk()
window.title("Haidar Dagham's Calculator program")  # Set the window title
window.geometry("500x500")  # Set the window size

equation_text = ""  # Variable to store the current input or expression
equation_label = StringVar()  # StringVar to dynamically update the label

# Create and display the label for the equation/output
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="grey", width=24, height=2)
label.pack()

# Create a frame to hold the buttons
frame = Frame(window)
frame.pack()

# Create number and operator buttons, arranged in a grid layout
button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

# Operator buttons
plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# Equals button to evaluate the expression
equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

# Decimal button for floating point numbers
decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

# Clear button to reset the input
clear = Button(window, text='clear', height=4, width=12, font=35, command=clear)
clear.pack()

window.mainloop()  # Run the Tkinter event loop