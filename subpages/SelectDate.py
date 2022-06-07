import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from subpages.DataBaseConnection import UserNamesHozoorGhiab, sabtHozoor,sabtGhayeb

current_directory = os.getcwd()


class MainDate:

    def __init__(self, datee):
        self.Date = datee

    def Registrationform(self):
        # window design
        reg_screen = Tk()
        reg_screen.title("فرم حضور غیاب گلبرگ دنیا")
        reg_screen.iconphoto(False, PhotoImage(file='images/logos.png'))
        reg_screen.geometry("400x400")

        Label(reg_screen, width="300", text= ' تاریخ انتخابی شما '+self.Date[0]+' و به صورت '+ self.Date[1]+' می‌باشد'
              , bg="purple", fg="white").pack(anchor='e')


        #  کلیک روی لیست حضور و غیاب

        global i
        i = 0
        global idPersons
        global PersonNames
        PersonNames, idPersons = UserNamesHozoorGhiab(self.Date)
        global lenPerson
        lenPerson = len(idPersons)

        def Virayesh():
            from subpages.EditDayUsers import Registrationform
            Registrationform(self.Date)
        # کلیک روی بازگشت و تغییر تاریخ
        def clickon3():
            MenueBazgasht()


        def barresieKoli():
            from subpages.treeviewSelectedDate import MaintreeViewSelectedDay
            maintreeView1 = MaintreeViewSelectedDay()
            maintreeView1.Registrationform(self.Date)

        if lenPerson == i:
            fram2 = tk.Frame(reg_screen, width=400, height=310, relief=SUNKEN, borderwidth=1)
            fram2.place(x=0, y=40)
            for widgets in fram2.winfo_children():
                widgets.destroy()
            Label(fram2, text="اطلاعات افراد در این تاریخ با موفقیت ثبت گردید\n \n"
                              "برای هر تغییری بر روی بررسی و ویرایش کلیک نمایید", fg='purple',
                  font=('bold', 14)).place(x=20, y=100)
            Bsabt = Button(fram2, text='بررسی کلی', width="17", bg='white', fg='purple', command=lambda: barresieKoli())
            Bsabt.place(x=135, y=230)
            Bsabt = Button(fram2, text=' ویرایش ', width="17", bg='white', fg='purple', command=lambda: Virayesh())
            Bsabt.place(x=135, y=260)
            B4 = Button(reg_screen, text=' بازگشت و تغییر تاریخ', command=lambda: clickon3(), bg='white', fg='black',
                        width="17")
            B4.place(x=135, y=350)
        else:
            def clickon0(i):
                B1.destroy()
                fram2 = tk.Frame(reg_screen, width=400, height=310, relief=SUNKEN, borderwidth=1)
                fram2.place(x=0, y=40)

                Bsabt = Button(fram2, text=' ثبت و ادامه', command=lambda: sabt(fram2,i), width="17", bg='white', fg='black')
                Bsabt.place(x=135, y=280)
                global idPerson
                global PersonName
                if lenPerson == i:
                    for widgets in fram2.winfo_children():
                        widgets.destroy()
                    Label(fram2, text="اطلاعات افراد در این تاریخ با موفقیت ثبت گردید\n \n"
                                      "برای هر تغییری بر روی بررسی و ویرایش کلیک نمایید", fg='purple',
                          font=('bold', 14)).place(x=5, y=100)
                    Bsabt = Button(fram2, text='بررسی کلی', width="17", bg='white', fg='purple',command=lambda: barresieKoli())
                    Bsabt.place(x=135, y=230)
                    Bsabt = Button(fram2, text=' ویرایش ', width="17", bg='white', fg='purple',command=lambda: Virayesh())
                    Bsabt.place(x=135, y=260)
                else:
                    PersonName = PersonNames[i]
                    idPerson = idPersons[i]
                    MenueHozoorGhayeb(fram2)




            B1 = Button(reg_screen, text=' لیست حضور و غیاب', command=lambda: clickon0(i), width="17", bg='white',
                        fg='black')
            B1.place(x=135, y=30)
            B4 = Button(reg_screen, text=' بازگشت و تغییر تاریخ', command=lambda: clickon3(), bg='white', fg='black',
                        width="17")
            B4.place(x=135, y=350)




            # MENUE 0  لیست حضور و غیاب
            def MenueHozoorGhayeb(fram2):
                MenueHozoorGhayebb(fram2,PersonName,PersonName)


            def MenueHozoorGhayebb(fram2, UserLists, PersonName):

                Label(fram2, text="نام کارمند ", anchor='e').place(x=330, y=5)
                Label(fram2, text=PersonName, anchor='e').place(x=220, y=5)
                Label(fram2, text="وضعیت", anchor='e').place(x=335, y=40)
                global State
                State = IntVar()
                Radiobutton(fram2, text="غایب", variable=State, value=0, command=lambda: ghayebSelected()).place(x=190,
                                                                                                                 y=40)
                Radiobutton(fram2, text="حاضر", variable=State, value=1, command=lambda: hozzorSelected(fram2)).place(x=250,
                                                                                                                      y=40)

                def ghayebSelected():
                    fram3 = tk.Frame(fram2, height=200, width=380)
                    fram3.place(x=20, y=70)
                    if fram3.winfo_ismapped() == 1:
                        fram3.destroy()

                def hozzorSelected(fram2):
                    global fram3
                    fram3 = tk.Frame(fram2, height=200, width=380)
                    fram3.place(x=20, y=70)
                    Label(fram3, text="تاخیر در ورود").place(x=265, y=6)
                    global StateTakhir
                    StateTakhir = IntVar()
                    Radiobutton(fram3, text="ندارد", variable=StateTakhir, value=0, command=lambda: nottakhir()).place(
                        x=200, y=5)
                    Radiobutton(fram3, text="دارد", variable=StateTakhir, value=1, command=lambda: takhir()).place(x=140,
                                                                                                                   y=5)

                    Label(fram3, text="مرخصی ساعتی").place(x=255, y=66)
                    global StateMorakhasi
                    StateMorakhasi = IntVar()
                    Radiobutton(fram3, text="ندارد", variable=StateMorakhasi, value=0, command=lambda: nomorakhasi()).place(
                        x=200,
                        y=65)
                    Radiobutton(fram3, text="دارد", variable=StateMorakhasi, value=1, command=lambda: morakhasi()).place(
                        x=140, y=65)

                    Label(fram3, text="اضافه کاری").place(x=275, y=126)
                    global StateEzafe
                    StateEzafe = IntVar()
                    Radiobutton(fram3, text="ندارد", variable=StateEzafe, value=0, command=lambda: noezafekari()).place(
                        x=200,
                        y=125)
                    Radiobutton(fram3, text="دارد", variable=StateEzafe, value=1, command=lambda: ezafekari()).place(x=140,
                                                                                                                     y=125)

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
                    TakhirM = Spinbox(fram4, from_=00, to=59, width=4)
                    TakhirM.place(x=140, y=7)
                    Label(fram4, text="ساعت تاخیر ").place(x=70, y=7)
                    global TakhirH
                    TakhirH = ttk.Combobox(fram4, values=("0", "1", "2", "3", "4", "5", "6", "7", "8"), width=4)
                    TakhirH.place(x=0, y=7)

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
                    Label(fram5, text="دقیقه مرخصی ").place(x=180, y=6)
                    MorakhasiM = Spinbox(fram5, from_=00, to=59, width=4)
                    MorakhasiM.place(x=140, y=7)
                    global MorakhasiH
                    Label(fram5, text="ساعت مرخصی ").place(x=56, y=6)
                    MorakhasiH = ttk.Combobox(fram5, values=("0", "1", "2", "3", "4", "5", "6", "7", "8"), width=4,
                                              state='readonly')
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
                    ezafekariM = Spinbox(fram6, from_=00, to=59, width=4)
                    ezafekariM.place(x=140, y=7)
                    global ezafekariH
                    Label(fram6, text="ساعت اضافه ").place(x=64, y=6)
                    ezafekariH = ttk.Combobox(fram6, values=("0", "1", "2", "3", "4", "5", "6", "7", "8"), width=4,
                                              state='readonly')
                    ezafekariH.place(x=0, y=5)

            def sabt(fram2,i):
                framErr = tk.Frame(fram2, height=35, width=400)
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
                                if len(takhH)==0:
                                    LableE.config(text='لطفا اطلاعات زمان تاخیر را وارد نمایید')
                                    LableE.place(x=100, y=8)
                                    Error = 1
                            elif ST == 0:
                                takhH = 0
                                takhM = 0

                            if SM == 1:  # agar morakhasi dasht
                                MorH = MorakhasiH.get()
                                MorM = MorakhasiM.get()
                                if len(MorH)==0:
                                    LableE.config(text='لطفا اطلاعات زمان مرخصی را وارد نمایید')
                                    LableE.place(x=100, y=8)
                                    Error = 1
                            elif SM == 0:
                                MorH = 0
                                MorM = 0

                            if SE == 1:  # agar ezafekari dasht
                                EzfH = ezafekariH.get()
                                EzfM = ezafekariM.get()
                                if  len(EzfH)==0:
                                    LableE.config(text='لطفا اطلاعات زمان اضافه کاری را وارد نمایید')
                                    LableE.place(x=85, y=8)
                                    Error = 1
                            elif SE == 0:
                                EzfH = 0
                                EzfM = 0
                            if Error == 0:
                                sabtHozoor(self.Date, idPerson[0], takhH, takhM, MorH, MorM, EzfH, EzfM)
                                LableE.config(text="اطلاعات با موفقیت ثبت گردید")
                                LableE.place(x=45, y=8)
                                i = i + 1
                                clickon0(i)
                        else:
                            LableE.config(text='لطفا اطلاعات حضور را تکمیل نمایید')
                            LableE.place(x=100, y=8)
                    else:
                        sabtGhayeb(self.Date,idPerson[0])
                        LableE.config(text="اطلاعات با موفقیت ثبت گردید")
                        LableE.place(x=45, y=8)
                        i = i + 1
                        clickon0(i)
                else:
                    LableE.config(text='لطفا وضعیت کارمند را مشخص نمایید')
                    LableE.place(x=100, y=8)
        # # MENUE 3  بازگشت و تغییر تاریخ
        def MenueBazgasht():
            reg_screen.destroy()
            from Main import Registrationform
            Registrationform()

        reg_screen.mainloop()



