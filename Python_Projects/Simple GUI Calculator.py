import tkinter as tk

calculation = ""


def AddtoCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)


def EvaluateCalculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except:
        ClearField()
        textResult.insert(1.0, "Error")


def ClearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


root = tk.Tk()
root.geometry("317x350")

textResult = tk.Text(root, height=1, width=13, font=("Arial", 32))
textResult.grid(columnspan=5)

btn1 = tk.Button(root, text="1", command=lambda: AddtoCalculation(1), width=4, font=("Arial", 20))
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: AddtoCalculation(2), width=4, font=("Arial", 20))
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: AddtoCalculation(3), width=4, font=("Arial", 20))
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: AddtoCalculation(4), width=4, font=("Arial", 20))
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: AddtoCalculation(5), width=4, font=("Arial", 20))
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: AddtoCalculation(6), width=4, font=("Arial", 20))
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: AddtoCalculation(7), width=4, font=("Arial", 20))
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: AddtoCalculation(8), width=4, font=("Arial", 20))
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: AddtoCalculation(9), width=4, font=("Arial", 20))
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: AddtoCalculation(0), width=4, font=("Arial", 20))
btn0.grid(row=5, column=2)

plus = tk.Button(root, text="+", command=lambda: AddtoCalculation("+"), width=4, font=("Arial", 20))
plus.grid(row=2, column=4)
minus = tk.Button(root, text="-", command=lambda: AddtoCalculation("-"), width=4, font=("Arial", 20))
minus.grid(row=3, column=4)
multiply = tk.Button(root, text="*", command=lambda: AddtoCalculation("*"), width=4, font=("Arial", 20))
multiply.grid(row=4, column=4)
divide = tk.Button(root, text="/", command=lambda: AddtoCalculation("/"), width=4, font=("Arial", 20))
divide.grid(row=5, column=4)

bracket1 = tk.Button(root, text="(", command=lambda: AddtoCalculation("("), width=4, font=("Arial", 20))
bracket1.grid(row=5, column=1)
bracket2 = tk.Button(root, text=")", command=lambda: AddtoCalculation(")"), width=4, font=("Arial", 20))
bracket2.grid(row=5, column=3)

equals = tk.Button(root, text="=", command=EvaluateCalculation, width=8, font=("Arial", 20))
equals.grid(row=6, column=3, columnspan=2)
clear = tk.Button(root, text="C", command=ClearField, width=8, font=("Arial", 20))
clear.grid(row=6, column=1, columnspan=2)

root.mainloop()