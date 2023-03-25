#!/usr/bin/python3
import random
from tkinter import *
import customtkinter
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
        global die
        
        lucktype = tk.IntVar()       
        mods = tk.IntVar()
        luck = tk.IntVar()
        mini = tk.IntVar()
        maxi = tk.IntVar()
        die = tk.IntVar()
        leftframe = customtkinter.CTkFrame(
        root
        )        
        leftframe.pack(side = LEFT, fill=X, anchor = NE, padx = 5)
        
        topframe = customtkinter.CTkFrame(
        root 
        )
        topframe.pack(side = TOP, fill=X)
                
        bottomframe = customtkinter.CTkFrame(
        root 
        )
        bottomframe.pack(side = TOP, fill=BOTH, pady = 5, expand=1)
                       
        l1 = customtkinter.CTkLabel(leftframe, text="Die min and max")
        l1.pack()
        self.entrythingy = customtkinter.CTkEntry(leftframe, placeholder_text="1")
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("1")
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy2 = customtkinter.CTkEntry(leftframe, placeholder_text="6")
        self.entrythingy2.pack()
        self.contents2 = tk.StringVar()
        self.contents2.set("6")
        self.entrythingy2["textvariable"] = self.contents2
         
        l2 = customtkinter.CTkLabel(leftframe, text="Modifiers (+ or -)")
        l2.pack()
        self.entrythingy3 = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.entrythingy3.pack()
        self.contents3 = tk.StringVar()
        self.contents3.set("")
        self.entrythingy3["textvariable"] = self.contents3
        
        l3 = customtkinter.CTkLabel(leftframe, text="Die To Roll")
        l3.pack()
        self.entrythingy4 = customtkinter.CTkEntry(leftframe, placeholder_text="1")
        self.entrythingy4.pack()
        self.contents4 = tk.StringVar()
        self.contents4.set("1")
        self.entrythingy4["textvariable"] = self.contents4  
                        
        c1 = customtkinter.CTkCheckBox(leftframe, text='Lucky',variable=luck, onvalue=True, offvalue=False)
        c1.pack()
        
        c2 = customtkinter.CTkCheckBox(leftframe, text='Lucky Removes 2\'s',variable=lucktype, onvalue=2, offvalue=1)
        c2.pack()  
             
        B = customtkinter.CTkButton(topframe, 
        text = 'Run Simulation',
        command = self.run, 
        font = ('Z003', 25),
        height=70, 
        width=100)
        B.pack()
        
        output = customtkinter.CTkTextbox(
        bottomframe,
        state='disabled',
        height = 400,
        width = 400
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
        die = self.entrythingy4.get() 
        attackroll.mini = mini
        attackroll.maxi = maxi
        attackroll.mods = mods
        attackroll.die = die
        self.setluck()
        self.setlucktype()
        attackroll.main()
        output.configure(state='normal')
        output.delete(1.0, END)
        str1 = attackroll.opt
        output.insert(END, str1)
        if attackroll.luck == True:
            str2 = attackroll.opt2
            output.insert(END, str2)  
        output.configure(state='disabled')  
            
if __name__ == "__main__":
    title = "RPG Die Thing"
    root = customtkinter.CTk(className = "RPGDT")
    root.geometry('500x450')
    myapp = App(root)
    myapp.master.title(title)
    myapp.mainloop()
