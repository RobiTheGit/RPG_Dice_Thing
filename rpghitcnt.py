#!/usr/bin/python3
import random
from tkinter import *
import tkinter as tk
import attackroll
global output
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        global luck
        global mini
        global maxi
        global mods
        global lucktype
        global output
        
        lucktype = tk.IntVar()       
        mods = tk.IntVar()
        luck = tk.IntVar()
        mini = tk.IntVar()
        maxi = tk.IntVar()
        
        l1 = tk.Label(text="Die min and max")
        l1.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("1")
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy2 = tk.Entry()
        self.entrythingy2.pack()
        self.contents2 = tk.StringVar()
        self.contents2.set("6")
        self.entrythingy2["textvariable"] = self.contents2
         
        l2 = tk.Label(text="Modifiers (+ or -)")
        l2.pack()
        self.entrythingy3 = tk.Entry()
        self.entrythingy3.pack()
        self.contents3 = tk.StringVar()
        self.contents3.set("")
        self.entrythingy3["textvariable"] = self.contents3
                   
        c1 = tk.Checkbutton(root, text='Lucky',variable=luck, onvalue=True, offvalue=False)
        c1.pack()
        
        c2 = tk.Checkbutton(root, text='Lucky Removes 2\'s',variable=lucktype, onvalue=2, offvalue=1)
        c2.pack()  
             
        B = tk.Button(root, 
        text = 'Run Simulation', 
        command = self.run, 
        height=3, 
        width=9)
        B.pack()
        
        output = tk.Text(
        root,
        state='normal',
        height = 400
        )  
        output.pack()
    def setluck(self):
        if luck.get() == True:
            attackroll.luck = True
            attackroll.lucktype = 0
        else:
            attackroll.luck = False
            
    def setlucktype(self):
        if lucktype.get() == 2:
            attackroll.lucktype = 2
        else:
            attackroll.lucktype = 1
    def run(self):
        mini = self.entrythingy.get()
        maxi = self.entrythingy2.get() 
        mods = self.entrythingy3.get() 
        attackroll.mini = mini
        attackroll.maxi = maxi
        attackroll.mods = mods
        self.setluck()
        self.setlucktype()
        attackroll.main()
        output.delete(1.0, END)
        str1 = attackroll.opt
        output.insert(END, str1)
        if attackroll.luck == True:
            str2 = attackroll.opt2
            output.insert(END, str2)        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    myapp = App(root)
    myapp.mainloop()
