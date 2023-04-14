#!/usr/bin/python3
import random
from tkinter import *
import customtkinter
import tkinter as tk
import attackroll
import sys
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
        global c2
        global toroll    
        photo = PhotoImage(file ="dieicon.png")
        root.iconphoto(False, photo)   
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
        l0 = customtkinter.CTkLabel(topframe, text="RPG Die Average Calculation Tool", font = ('Z003', 20))
        l0.pack()
                               
        l1 = customtkinter.CTkLabel(leftframe, text="Die min and max", font = ('Z003', 16))
        l1.pack()
        self.entrythingy = customtkinter.CTkEntry(leftframe, placeholder_text="1", font = ('Z003', 16))
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("1")
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy2 = customtkinter.CTkEntry(leftframe, placeholder_text="6", font = ('Z003', 16))
        self.entrythingy2.pack()
        self.contents2 = tk.StringVar()
        self.contents2.set("6")
        self.entrythingy2["textvariable"] = self.contents2
         
        l2 = customtkinter.CTkLabel(leftframe, text="Modifiers (+ or -)", font = ('Z003', 16))
        l2.pack()
        self.entrythingy3 = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 16))
        self.entrythingy3.pack()
        self.contents3 = tk.StringVar()
        self.contents3.set("")
        self.entrythingy3["textvariable"] = self.contents3
        
        l3 = customtkinter.CTkLabel(leftframe, text="Die To Roll", font = ('Z003', 16))
        l3.pack()
        self.entrythingy4 = customtkinter.CTkEntry(leftframe, placeholder_text="1", font = ('Z003', 16))
        self.entrythingy4.pack()
        self.contents4 = tk.StringVar()
        self.contents4.set("1")
        self.entrythingy4["textvariable"] = self.contents4 
        
        l3 = customtkinter.CTkLabel(leftframe, text="How many times are the die rolled", font = ('Z003', 16))
        l3.pack()         
        self.entrythingy5 = customtkinter.CTkEntry(leftframe, placeholder_text="1", font = ('Z003', 16))
        self.entrythingy5.pack()
        self.contents5 = tk.StringVar()
        self.contents5.set("1")
        self.entrythingy5["textvariable"] = self.contents5  
                               
        c1 = customtkinter.CTkCheckBox(leftframe, text='Lucky',variable=luck, onvalue=True, offvalue=False, command=self.enablelr2s, font = ('Z003', 16))
        c1.pack()
        
        c2 = customtkinter.CTkCheckBox(leftframe, text='Lucky Removes 2\'s',variable=lucktype, onvalue=2, offvalue=1, state='disabled', font = ('Z003', 16))
        c2.pack()  
             
        B = customtkinter.CTkButton(topframe, 
        text = 'Run Simulation',
        command = self.run, 
        font = ('Z003', 25),
        height=70, 
        width=100)
        B.pack()
        
        blank = customtkinter.CTkLabel(leftframe, text="\n")
        blank.pack() 
            
        exitbutton = customtkinter.CTkButton(
        leftframe,
        text = '        Exit        ',
        command = self.exit, 
        font = ('Z003', 25),
        height=3,
        width=8)
        exitbutton.pack(side = BOTTOM, anchor = SE)
                
        output = customtkinter.CTkTextbox(
        bottomframe,
        state='disabled',
        height = 400,
        width = 400
        )  
        output.pack()
    def enablelr2s(self):
        global c2
        if luck.get() == True:
            c2.configure(state='normal')
            c2.update()
        else:
            c2.configure(state='disabled')
            c2.update()
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
    def exit(self):
        sys.exit(0)            
    def run(self):
        mini = self.entrythingy.get()
        maxi = self.entrythingy2.get() 
        mods = self.entrythingy3.get() 
        die = self.entrythingy4.get() 
        toroll = self.entrythingy5.get()
        attackroll.mini = mini
        attackroll.maxi = maxi
        attackroll.mods = mods
        attackroll.die = die
        attackroll.toroll = toroll
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
    title = "RPG Die Tool"
    root = customtkinter.CTk(className = "Rpg Die Tool")
    root.geometry('500x450')
    myapp = App(root)
    myapp.master.title(title)
    myapp.mainloop()
