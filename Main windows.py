from tkinter import *
import tkinter.ttk as tkr

import sqlite3

# ----------------- WINDOW TO CHANGE ------------------------------#

class windows1:

    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.root.config(bg="grey")
        self.root.columnconfigure(0, weight=1)

        self.fram = Frame(root)
        self.fram
        self.fram.config(bg='blue')
        
        self.fram.grid(row=0, column=0, columnspan=2)
       
        

        self.fram1 = Frame(root)
        self.fram1.config(bg='blue')
        self.fram1.grid(row=1, column=0)
        self.fram1.grid_rowconfigure(1, weight=1)
        self.fram1.grid_columnconfigure(0, weight=1)

        self.fram2 = Frame(root)
        self.fram2.config(bg='BLUE')
        self.fram2.grid(row=1, column=1,sticky=N+S)
        


        def openwindows1():
            top = Toplevel()
            windows2(top)

        def openwindows2():
            top = Toplevel()
            windows3(top)

        def openwindows3():
            top = Toplevel()
            windows4(top)

        self.Label = Label(self.fram,text="COVID-19 IN UNITED STATES OF AMERICA",bg="grey",font=("Arial",27)).grid(row=0,column=0,sticky=W+E,ipady=15)
        self.Label = Label(self.fram1,text="test",bg="grey",font=("Arial",27)).grid(row=0,column=0,sticky=W+E,ipady=15)
        self.button1 = Button(self.fram2,text="Covid-19 progression within greatest States",command= openwindows1)
        self.button2 = Button(self.fram2,text="Covid-19 progression",command= openwindows2)
        self.button3 = Button(self.fram2,text="Individual Analysis of US states ",command= openwindows3)
        
        self.button1.grid(row=0, column=0,ipady=5)
        self.button2.grid(row=1, column=0,ipady=5,pady=5)
        self.button3.grid(row=2, column=0,ipady=5)

        
    

        

    
     
            
# ----------------- WINDOW TO CHANGE ------------------------------#
class windows2:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.framtable = Frame(self.root)
        self.root.config(bg="grey")

class windows3:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.framtable = Frame(self.root)
        self.root.config(bg="grey")

class windows4:
    def __init__(self, root):
        self.root = root
        self.root.title("Covid-19")
        self.root.geometry("1000x600")
        self.framtable = Frame(self.root)
        self.root.config(bg="grey")

       


        

        


root = Tk()
ins = windows1(root)
# omg = Addwindows(root)
root.mainloop()
