from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from subpages.DataBaseConnection import UserNames

def MenueVaziateKarmand(reg_screen):

    def barresi(n, idList, cb, monthsbox, Year, UserS):
        if monthsbox == '' or cb == -1:
            Label(text='  !!! لطفا تمام مقادیر را انتخاب نمایید !!! ', fg="purple").place(x=260, y=150)
        else:
            names = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور'
                , 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
            MonNumber = names.index(monthsbox) + 1

            if n == 1:
                from subpages.treeviewTotal import MaintreeViewTotal
                maintreeView1 = MaintreeViewTotal()
                maintreeView1.Registrationform(idList[cb], Year, MonNumber, UserS)
            else:
                from subpages.treeviewDetail import MaintreeViewDetail
                maintreeView2 = MaintreeViewDetail()
                maintreeView2.Registrationform(idList[cb], Year, MonNumber, UserS)

    fram2 = tk.Frame(reg_screen, width=450, height=340, relief=SUNKEN, borderwidth=1)
    fram2.place(x=150, y=40)
    Label(fram2, text="نام کارمند ").place(x=390, y=27, anchor='e')
    UserLists, idList = UserNames()
    data = UserLists
    cb = ttk.Combobox(fram2, values=data)
    cb.place(x=100, y=20)
    Label(fram2, text="انتخاب ماه و سال").place(x=390, y=70, anchor='e')
    Sp = Spinbox(fram2, from_=1400, to=1500, width=5)
    Sp.place(x=100, y=65)
    Monthsbox = ttk.Combobox(fram2,
                             values=('فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر',
                                     'دی', 'بهمن', 'اسفند'), width=8, justify=RIGHT)
    Monthsbox.place(x=180, y=65)
    Bsabt = Button(fram2, text=' بررسی وضعیت کلی ماه', command=lambda: barresi(1, idList, cb.current(), Monthsbox.get()
                                                                               , Sp.get(), cb.get()), width=" 17",
                   bg='white', fg='black')
    Bsabt.place(x=150, y=150)
    Bsabt2 = Button(fram2, text=' بررسی جزئیات ماهانه', command=lambda: barresi(2, idList, cb.current(), Monthsbox.get()
                                                                                , Sp.get(), cb.get()), width="17",
                    bg='white', fg='black')
    Bsabt2.place(x=150, y=190)
