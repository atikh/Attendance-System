import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import sys
import sqlite3
from subpages.DataBaseConnection import UserNames, getAllValues

DbName = "DB/GolbargDonya.db"


def Registrationform(dateinput):
    global Dat
    Dat = dateinput[0]
    global reg_screen
    reg_screen = Tk()
    for widgets in reg_screen.winfo_children():
        widgets.destroy()
    reg_screen.title("ویرایش اطلاعات حضور و غیاب")
    reg_screen.geometry("340x150")
    Label(reg_screen, text="نام کارمند ").place(x=255, y=30)
    UserLists, idList = UserNames()
    data = UserLists
    cb = ttk.Combobox(reg_screen, values=data)
    cb.place(x=70, y=30)
    B1 = Button(reg_screen, text="انتخاب و ادامه", width=10, height=1, bg="purple", fg="white",
                command=lambda: choose())
    B1.place(x=120, y=75)

    B5 = Button(reg_screen, text="ویرایش نوع روز برای تمامی افراد", width=25, height=1, bg="purple", fg="white",
                command=lambda: changeDayType())
    B5.place(x=70, y=105)
    Ltop = Label(reg_screen, width="300", text="لطفا کارمند مورد نظر را انتخاب نمایید", bg="purple", fg="white")
    Ltop.pack(anchor='e')

    def SubmitDaytype(Daytype):
        from subpages.DataBaseConnection import updateDayType
        if Daytype=='':
            Label(reg_screen, text=' نوع روز را مشخص نمایید ', fg='purple').place(x=90, y=90)
        else:
            updateDayType(Dat, Daytype)
            Label(reg_screen, text=' نوع روز با موفقیت تغییر یافت ', fg='purple').place(x=90, y=90)
            reg_screen.after(1000, lambda: reg_screen.destroy())

    def changeDayType():
        for widgets in reg_screen.winfo_children():
            widgets.destroy()
        reg_screen.geometry("340x150")
        Ltop = Label(reg_screen, width="300", text="لطفا نوع روز مورد نظر را انتخاب نمایید", bg="purple", fg="white")
        Ltop.pack(anchor='e')
        reg_screen.title("ویرایش نوع روز برای تمامی کاربران")
        from subpages.DataBaseConnection import findDate
        dateinf = findDate(Dat)
        daytp = StringVar()
        dayType = ttk.Combobox(reg_screen, width=20, textvariable=daytp, justify='right')
        LableDay = Label(reg_screen, text='')
        LableDay.place(x=200, y=30)
        LableDay.config(text='نوع روز تعیین شده ')
        dateinff = dateinf[0]
        Label(reg_screen, text=dateinff[0]).place(x=50, y=30)

        Label(reg_screen, text='تغییر به').place(x=250, y=60)
        dayType['values'] = (' روز کاری ', ' روز تعطیل با حقوق ', ' روز تعطیل بدون حقوق',)
        dayType.current()
        dayType.place(x=30, y=60)

        B2 = Button(reg_screen, text="ذخیره‌ی تغییرات", width=10, height=1, bg="purple", fg="white",
                    command=lambda: SubmitDaytype(dayType.get()))
        B2.place(x=180, y=110)

        B2 = Button(reg_screen, text="لغو  بازگشت", width=10, height=1, bg="purple", fg="white",
                    command=lambda: cancel())
        B2.place(x=80, y=110)

    def choose():
        if cb.get() == '':
            Label(reg_screen, text="!! لطفا فردی را انتخاب نمایید !!", anchor='e', fg='purple').place(x=90, y=55)
        else:
            DayType, YN, TakhirHin, TakhirMin, MorakhasiHin, MorakhasiMin, EzafekariHin, EzafekariMin, IDDate = getAllValues(
                idList, cb.current(), Dat)
            NameSelected = cb.get()
            for widgets in reg_screen.winfo_children():
                widgets.destroy()
            Ltop = Label(reg_screen, width="300", text=NameSelected, bg="purple", fg="white")
            Ltop.pack(anchor='e')

            reg_screen.geometry("340x320")
            B2 = Button(reg_screen, text="ذخیره‌ی تغییرات", width=10, height=1, bg="purple", fg="white",
                        command=lambda: sabtt(IDDate))
            B2.place(x=180, y=280)

            B2 = Button(reg_screen, text="لغو  بازگشت", width=10, height=1, bg="purple", fg="white",
                        command=lambda: cancel())
            B2.place(x=80, y=280)

            def ghayebSelected():
                fram3 = tk.Frame(reg_screen, height=200, width=380)
                fram3.place(x=20, y=70)
                if fram3.winfo_ismapped() == 1:
                    fram3.destroy()

            def hozzorSelected():
                global fram3
                fram3 = tk.Frame(reg_screen, height=200, width=380)
                fram3.place(x=20, y=70)
                Label(fram3, text="تاخیر در ورود").place(x=215, y=6)

                def nottakhir():
                    fram4 = tk.Frame(fram3, height=35, width=360)
                    fram4.place(x=0, y=30)
                    if fram4.winfo_ismapped() == 1:
                        fram4.destroy()

                def takhir():
                    global fram4
                    fram4 = tk.Frame(fram3, height=35, width=360)
                    fram4.place(x=0, y=30)
                    Label(fram4, text="دقیقه تاخیر ").place(x=195, y=7)
                    global TakhirM
                    Defaulttakhir = IntVar(reg_screen)
                    if TakhirMin > 0:
                        Defaulttakhir.set(TakhirMin)
                    TakhirM = Spinbox(fram4, from_=00, to=59, width=4, textvariable=Defaulttakhir)
                    TakhirM.place(x=140, y=7)
                    Label(fram4, text="ساعت تاخیر ").place(x=70, y=7)
                    global TakhirH
                    DefaulttakhirH = IntVar(reg_screen)
                    if TakhirHin > 0:
                        DefaulttakhirH.set(TakhirHin)
                    TakhirH = Spinbox(fram4, from_=0, to=8, width=4, textvariable=DefaulttakhirH)
                    TakhirH.place(x=0, y=7)

                global StateTakhir
                StateTakhir = IntVar(reg_screen)
                if TakhirHin == 0 and TakhirMin == 0:
                    StateTakhir.set(0)
                elif TakhirHin > 0 or TakhirMin > 0:
                    StateTakhir.set(1)
                    takhir()
                Radiobutton(fram3, text="ندارد", variable=StateTakhir, value=0, command=lambda: nottakhir()).place(
                    x=140, y=5)
                Radiobutton(fram3, text="دارد", variable=StateTakhir, value=1, command=lambda: takhir()).place(x=90,
                                                                                                               y=5)

                Label(fram3, text="مرخصی ساعتی").place(x=205, y=66)
                global StateMorakhasi
                StateMorakhasi = IntVar(reg_screen)
                if MorakhasiHin == 0 and MorakhasiMin == 0:
                    StateMorakhasi.set(0)
                elif MorakhasiHin > 0 or MorakhasiMin > 0:
                    StateMorakhasi.set(1)
                    morakhasi()
                Radiobutton(fram3, text="ندارد", variable=StateMorakhasi, value=0, command=lambda: nomorakhasi()).place(
                    x=140, y=65)
                Radiobutton(fram3, text="دارد", variable=StateMorakhasi, value=1, command=lambda: morakhasi()).place(
                    x=90, y=65)

                Label(fram3, text="اضافه کاری").place(x=225, y=126)
                global StateEzafe
                StateEzafe = IntVar(reg_screen)
                if EzafekariHin == 0 and EzafekariMin == 0:
                    StateEzafe.set(0)
                elif EzafekariHin > 0 or EzafekariMin > 0:
                    StateEzafe.set(1)
                    ezafekari()
                Radiobutton(fram3, text="ندارد", variable=StateEzafe, value=0, command=lambda: noezafekari()).place(
                    x=140, y=125)
                Radiobutton(fram3, text="دارد", variable=StateEzafe, value=1, command=lambda: ezafekari()).place(x=90,
                                                                                                                 y=125)

            def nomorakhasi():
                global fram5
                fram5 = tk.Frame(fram3, height=35, width=360)
                fram5.place(x=0, y=90)
                if fram5.winfo_ismapped() == 1:
                    fram5.destroy()

            def morakhasi():
                global fram5
                fram5 = tk.Frame(fram3, height=35, width=360)
                fram5.place(x=0, y=90)
                global MorakhasiM
                Defaultmorakhasi = IntVar(reg_screen)
                if MorakhasiMin > 0:
                    Defaultmorakhasi.set(MorakhasiMin)
                Label(fram5, text="دقیقه مرخصی ").place(x=180, y=6)
                MorakhasiM = Spinbox(fram5, from_=00, to=59, width=4, textvariable=Defaultmorakhasi)
                MorakhasiM.place(x=140, y=7)

                Label(fram5, text="ساعت مرخصی ").place(x=56, y=6)
                global MorakhasiH
                DefaultmorakhasiH = IntVar(reg_screen)
                if MorakhasiHin > 0:
                    DefaultmorakhasiH.set(MorakhasiHin)
                MorakhasiH = Spinbox(fram5, from_=0, to=8, width=4, textvariable=DefaultmorakhasiH)
                MorakhasiH.place(x=0, y=5)

            def noezafekari():
                global fram6
                fram6 = tk.Frame(fram3, height=35, width=360)
                fram6.place(x=0, y=150)
                if fram6.winfo_ismapped() == 1:
                    fram6.destroy()

            def ezafekari():
                global fram6
                fram6 = tk.Frame(fram3, height=35, width=360)
                fram6.place(x=0, y=150)
                global ezafekariM
                Label(fram6, text="دقیقه اضافه‌ ").place(x=185, y=6)
                DefaulezafeH = IntVar(reg_screen)
                if EzafekariMin > 0:
                    DefaulezafeH.set(EzafekariMin)
                ezafekariM = Spinbox(fram6, from_=00, to=59, width=4, textvariable=DefaulezafeH)
                ezafekariM.place(x=140, y=7)
                global ezafekariH
                Label(fram6, text="ساعت اضافه ").place(x=64, y=6)
                DefaulezafeM = IntVar(reg_screen)
                if EzafekariHin > 0:
                    DefaulezafeM.set(EzafekariHin)
                ezafekariH = Spinbox(fram6, from_=0, to=8, width=4, textvariable=DefaulezafeM)
                ezafekariH.place(x=0, y=5)

            Label(reg_screen, text="وضعیت", anchor='e').place(x=260, y=40)
            global State
            State = IntVar(reg_screen)
            if YN == 0:
                State.set(0)
            elif YN == 1:
                State.set(1)
                hozzorSelected()
            Radiobutton(reg_screen, text="غایب", variable=State, value=0, command=lambda: ghayebSelected()).place(x=130,
                                                                                                                  y=40)
            Radiobutton(reg_screen, text="حاضر", variable=State, value=1, command=lambda: hozzorSelected()).place(x=190,
                                                                                                                  y=40)

    def cancel():
        reg_screen.destroy()
        Registrationform(dateinput)

    def sabtt(IDDate):
        framErr = tk.Frame(reg_screen, height=35, width=400)
        framErr.place(x=10, y=245)
        LableE = Label(framErr, fg='purple')
        SH = State.get()
        if SH in (0, 1):
            if SH == 1:  # agar haze bood
                ST = StateTakhir.get()
                SM = StateMorakhasi.get()
                SE = StateEzafe.get()
                if ST in (0, 1) and SM in (0, 1) and SE in (0, 1):  # agar hame ro meghdar dad ok
                    Error = 0
                    if ST == 1:  # agar takhir dasht
                        takhH = TakhirH.get()
                        takhM = TakhirM.get()
                        if takhM == 0 and takhH == 0:
                            LableE.config(text='لطفا اطلاعات زمان تاخیر را وارد نمایید')
                            LableE.place(x=100, y=8)
                            Error = 1
                    elif ST == 0:
                        takhH = 0
                        takhM = 0

                    if SM == 1:  # agar morakhasi dasht
                        MorH = MorakhasiH.get()
                        MorM = MorakhasiM.get()
                        if MorH == 0 and MorM == 0:
                            LableE.config(text='لطفا اطلاعات زمان مرخصی را وارد نمایید')
                            LableE.place(x=100, y=8)
                            Error = 1
                    elif SM == 0:
                        MorH = 0
                        MorM = 0

                    if SE == 1:  # agar ezafekari dasht
                        EzfH = ezafekariH.get()
                        EzfM = ezafekariM.get()
                        if EzfH == 0 and EzfM == 0:
                            LableE.config(text='لطفا اطلاعات زمان اضافه کاری را وارد نمایید')
                            LableE.place(x=85, y=8)
                            Error = 1
                    elif SE == 0:
                        EzfH = 0
                        EzfM = 0
                    if Error == 0:
                        query = "UPDATE Date SET YN =? ,TakhirH =? ,TakhirM=?, MorakhasiH=?, MorakhasiM=?, EzafekariH=?, EzafekariM=? WHERE ID =?"
                        Params = (1, takhH, takhM, MorH, MorM, EzfH, EzfM, IDDate)
                        with sqlite3.connect(DbName) as connection:
                            cursor = connection.cursor()
                            cursor.execute(query, Params)
                            connection.commit()
                            LableE.config(text="اطلاعات با موفقیت ثبت گردید")
                            LableE.place(x=85, y=8)
                            reg_screen.after(1000, lambda: reg_screen.destroy())
                else:
                    LableE.config(text='لطفا اطلاعات حضور را تکمیل نمایید')
                    LableE.place(x=100, y=8)
            else:
                query = "UPDATE Date SET (YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM, EzafekariH, EzafekariM) WHERE ID Values(?,?,?,?,?,?,?,?,?,?)"
                Params = (0, 0, 0, 0, 0, 0, 0, 0)
                with sqlite3.connect(DbName) as connection:
                    cursor = connection.cursor()
                    cursor.execute(query, Params)
                    connection.commit()
                    LableE.config(text="اطلاعات با موفقیت ثبت گردید")
                    LableE.place(x=45, y=8)
                    reg_screen.after(1000, lambda: reg_screen.destroy())

        else:
            LableE.config(text='لطفا وضعیت کارمند را مشخص نمایید')
            LableE.place(x=100, y=8)

    reg_screen.mainloop()
