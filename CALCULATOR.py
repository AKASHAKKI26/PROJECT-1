from tkinter import *
class calc:
    def __init__(self,a):
        a.title("Calculator")
        a.geometry("350x400+0+0")
        a.bg='gray'         
        a.resizable(False,False)

        self.equation=StringVar()
        self.e_value= ' '
        Entry(width=17, bg='grey',font=("Arial Bold", 28),textvariable=self.equation).place(x=0,y=0)

        Button(width=10,height=5,text="(",bg="white",command=lambda:self.show('(')).place(x=0 ,y=50)
        Button(width=10,height=5,text=")",bg="white",command=lambda:self.show(')')).place(x=90 ,y=50)
        Button(width=10,height=5,text="%",bg="white",command=lambda:self.show('%')).place(x=180 ,y=50 )
        Button(width=10,height=5,text="1",bg="white",command=lambda:self.show(1)).place(x=0 ,y=125 )
        Button(width=10,height=5,text="2",bg="white",command=lambda:self.show(2)).place(x=90 ,y=125 )
        Button(width=10,height=5,text="3",bg="white",command=lambda:self.show(3)).place(x=180 ,y=125 )
        Button(width=10,height=5,text="4",bg="white",command=lambda:self.show(4)).place(x=0 ,y=200 )
        Button(width=10,height=5,text="5",bg="white",command=lambda:self.show(5)).place(x=90 ,y=200 )
        Button(width=10,height=5,text="6",bg="white",command=lambda:self.show(6)).place(x=180 ,y=200 )
        Button(width=10,height=5,text="7",bg="white",command=lambda:self.show(7)).place(x=0 ,y=275 )
        Button(width=10,height=5,text="8",bg="white",command=lambda:self.show(8)).place(x=180,y=275 )
        Button(width=10,height=5,text="9",bg="white",command=lambda:self.show(9)).place(x=90 ,y=275 )
        Button(width=10,height=5,text="0",bg="white",command=lambda:self.show(0)).place(x=90 ,y=350 )
        Button(width=10,height=5,text=".",bg="white",command=lambda:self.show('.')).place(x=180 ,y=350 )
        Button(width=10,height=5,text="+",bg="white",command=lambda:self.show('+')).place(x=270 ,y=275 )
        Button(width=10,height=5,text="-",bg="white",command=lambda:self.show('-')).place(x=270 ,y=200 )
        Button(width=10,height=5,text="/",bg="white",command=lambda:self.show('/')).place(x=270 ,y=50 )
        Button(width=10,height=5,text="",bg="white",command=lambda:self.show('')).place(x=270 ,y=125 )
        Button(width=10,height=5,text="=",bg="white",command=self.solve).place(x=270 ,y=350 )
        Button(width=10,height=5,text="C",command=self.clear).place(x=0,y=350 )

    def show(self,value):
            self.e_value+=str(value)
            self.equation.set(self.e_value)
    def clear(self):
        self.e_value=' '
        self.equation.set(self.e_value)
    def solve(self):
        try:
            result = eval(self.e_value)
            self.equation.set(result)
            self.e_value = str(result)
        except:
            self.equation.set("Error")
            self.e_value = ''

root=Tk()
calculator=calc(root)
root.mainloop()