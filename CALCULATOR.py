from tkinter import *

class calc:
    def __init__(self, a):
        a.title("Calculator")
        a.geometry("350x430+0+0")
        a.configure(bg='gray')         
        a.resizable(False, False)
        self.equation = StringVar()
        self.e_value = ''

        Entry(a, font=("Arial Bold", 24), bg='lightgray', textvariable=self.equation, justify='right').place(x=10, y=10, width=330, height=50)
        Button(a, text="(", bg="white", command=lambda: self.show('(')).place(x=10, y=70, width=75, height=60)
        Button(a, text=")", bg="white", command=lambda: self.show(')')).place(x=90, y=70, width=75, height=60)
        Button(a, text="%", bg="white", command=lambda: self.show('%')).place(x=170, y=70, width=75, height=60)
        Button(a, text="/", bg="white", command=lambda: self.show('/')).place(x=250, y=70, width=75, height=60)
        Button(a, text="1", bg="white", command=lambda: self.show(1)).place(x=10, y=140, width=75, height=60)
        Button(a, text="2", bg="white", command=lambda: self.show(2)).place(x=90, y=140, width=75, height=60)
        Button(a, text="3", bg="white", command=lambda: self.show(3)).place(x=170, y=140, width=75, height=60)
        Button(a, text="*", bg="white", command=lambda: self.show('*')).place(x=250, y=140, width=75, height=60)
        Button(a, text="4", bg="white", command=lambda: self.show(4)).place(x=10, y=210, width=75, height=60)
        Button(a, text="5", bg="white", command=lambda: self.show(5)).place(x=90, y=210, width=75, height=60)
        Button(a, text="6", bg="white", command=lambda: self.show(6)).place(x=170, y=210, width=75, height=60)
        Button(a, text="-", bg="white", command=lambda: self.show('-')).place(x=250, y=210, width=75, height=60)
        Button(a, text="7", bg="white", command=lambda: self.show(7)).place(x=10, y=280, width=75, height=60)
        Button(a, text="8", bg="white", command=lambda: self.show(8)).place(x=90, y=280, width=75, height=60)
        Button(a, text="9", bg="white", command=lambda: self.show(9)).place(x=170, y=280, width=75, height=60)
        Button(a, text="+", bg="white", command=lambda: self.show('+')).place(x=250, y=280, width=75, height=60)
        Button(a, text="C", bg="white", command=self.clear).place(x=10, y=350, width=75, height=60)
        Button(a, text="0", bg="white", command=lambda: self.show(0)).place(x=90, y=350, width=75, height=60)
        Button(a, text=".", bg="white", command=lambda: self.show('.')).place(x=170, y=350, width=75, height=60)
        Button(a, text="=", bg="white", command=self.solve).place(x=250, y=350, width=75, height=60)

    def show(self, value):
        self.e_value += str(value)
        self.equation.set(self.e_value)

    def clear(self):
        self.e_value = ''
        self.equation.set(self.e_value)

    def solve(self):
        try:
            result = eval(self.e_value)
            self.equation.set(result)
            self.e_value = str(result)
        except:
            self.equation.set("Error")
            self.e_value = ''

root = Tk()
calculator = calc(root)
root.mainloop()
