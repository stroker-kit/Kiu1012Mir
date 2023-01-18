import tkinter as tk
from tkinter import *
def main():
        def add_digit(digit):
            value=calc.get()+str(digit)
            calc.delete(0,tk.END)
            calc.insert(0,value)
            print(value,digit)
            if digit=="=":
                x = value
                x = x.replace("=", "")
                print(x)
                x = x.split("+")
                if len(x)==2:
                 x = int(x[0]) + int(x[1])
                 print(value, x)
                 x = str(x)
                 calc.delete(0, tk.END)
                 calc.insert(0, x)
                x=str(x[0])
                x = x.split("*")
                print(x)
                if len(x)==2:
                    x = int(x[0]) * int(x[1])
                    print(value, x)
                    x = str(x)
                    print(x)
                    calc.delete(0, tk.END)
                    calc.insert(0, x)
                x = str(x[0])
                x = x.split("/")
                print(x)
                if len(x)==2:
                    x = int(x[0]) / int(x[1])
                    print(value, x)
                    x = str(x)
                    calc.delete(0, tk.END)
                    calc.insert(0, x)
            if digit=="AC":
                calc.delete(0, tk.END)
                calc.insert(0,'')





        window = tk.Tk()
        window.geometry("270x230")
        window.title("Калькулятор")
        calc=tk.Entry(window,justify=RIGHT)
        calc.grid(row=0,column=1,columnspan=4)
        tk.Button(text="1",bd=2,command=lambda:add_digit(1)).grid(row=1,column=1,stick="wens")
        tk.Button(text="2",bd=2,command=lambda:add_digit(2)).grid(row=1,column=2,stick="wens")
        tk.Button(text="3",bd=2,command=lambda:add_digit(3)).grid(row=1,column=3,stick="wens")
        tk.Button(text="4",bd=2,command=lambda:add_digit(4)).grid(row=2,column=1,stick="wens")
        tk.Button(text="5",bd=2,command=lambda:add_digit(5)).grid(row=2,column=2,stick="wens")
        tk.Button(text="6",bd=2,command=lambda:add_digit(6)).grid(row=2,column=3,stick="wens")
        tk.Button(text="7",bd=2,command=lambda:add_digit(7)).grid(row=3,column=1,stick="wens")
        tk.Button(text="8",bd=2,command=lambda:add_digit(8)).grid(row=3,column=2,stick="wens")
        tk.Button(text="9",bd=2,command=lambda:add_digit(9)).grid(row=3,column=3,stick="wens")
        tk.Button(text="0",bd=2,command=lambda:add_digit(0)).grid(row=4,column=1,stick="wens")
        window.grid_columnconfigure(1,minsize=60)
        window.grid_columnconfigure(2,minsize=60)
        window.grid_columnconfigure(3,minsize=60)
        window.grid_rowconfigure(1,minsize=60)
        window.grid_rowconfigure(2,minsize=60)
        window.grid_rowconfigure(3,minsize=60)
        window.grid_rowconfigure(4,minsize=60)

        tk.Button(text="+",bd=2,command=lambda:add_digit("+")).grid(row=1,column=4,stick="wens")
        tk.Button(text="-",bd=2,command=lambda:add_digit("-")).grid(row=2,column=4,stick="wens")
        tk.Button(text="*",bd=2,command=lambda:add_digit("*")).grid(row=3,column=4,stick="wens")
        window.grid_rowconfigure(6,minsize=60)
        tk.Button(text="/",bd=2,command=lambda:add_digit("/")).grid(row=4,column=3,stick="wens")
        tk.Button(text="AC",bd=2,command=lambda:add_digit("AC")).grid(row=4,column=2,stick="wens")
        tk.Button(text="=",bd=2,command=lambda:add_digit("=")).grid(row=4,column=4,stick="wens")
        window.grid_rowconfigure(7,minsize=60)
        window.mainloop()
main()
