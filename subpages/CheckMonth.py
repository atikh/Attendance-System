import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
DbName = "DB/GolbargDonya.db"



def Registrationform():
    # window design
    reg_screen = Tk()
    reg_screen.title("فرم حضور غیاب گلبرگ دنیا")
    reg_screen.iconphoto(False, PhotoImage(file='../images/logos.png'))
    reg_screen.geometry("400x600")

    Label(reg_screen, width="300", text= '', bg="purple", fg="white").pack(anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.pack(anchor='n')
    panedwindow = ttk.Panedwindow(reg_screen, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Create Frams
    d = {}
    f={}
    for i in range(1, 32):
        d["RFrame{0}".format(i)] = ttk.Frame(reg_screen, width=90, height=20, relief=SUNKEN)
        f1Y=((i-1)*20)
        d["RFrame{0}".format(i)] .place(x=0,y=f1Y)
        f["LFrame".format(i)] = ttk.Frame(reg_screen, width=340, height=20, relief=SUNKEN)
        f["LFrame".format(i)].place(x=90,y=f1Y)


    reg_screen.mainloop()





Registrationform()