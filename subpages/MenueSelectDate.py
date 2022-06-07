
from tkinter import *
from subpages.Jalalicalendarwidget import JCalendar
from tkinter import ttk
import tkinter as tk
from subpages.SelectDate import MainDate


def menueSelectDate(reg_screen):

    fram2 = tk.Frame(reg_screen, width=450, height=340, relief=SUNKEN, borderwidth=1)
    fram2.place(x=150, y=40)

    fram3 = tk.Frame(fram2, width=450, height=50, relief=SUNKEN)
    fram3.place(x=0, y=240)

    daytp = StringVar()


    def submit(selectedDate,dateinf):
        if daytp.get() == '' and len(dateinf)==0:
           Label(fram2, text="!! لطفا نوع روز را مشخص کنید !!", foreground='purple').place(x=100, y=315)
        else:
            datee = [selectedDate, daytp.get()]
            reg_screen.destroy()
            mainui = MainDate(datee)
            mainui.Registrationform()


    def validate():
        if calendar.selection is None:
            for widgets in fram3.winfo_children():
                widgets.destroy()
            Label(fram3, text="!! لطفا یک روز را انتخاب کنید !!", foreground='purple').place(x=150, y=10)
        elif calendar.selection is not None:
            year, month, day= calendar.selection
            if year is not None:
                SelectedDate=str(day)+'/'+str(month)+'/'+str(year)
                for widgets in fram3.winfo_children():
                    widgets.destroy()
                from subpages.DataBaseConnection import findDate
                dateinf=findDate(SelectedDate)
                dayType = ttk.Combobox(fram3, width=20, textvariable=daytp, justify='right')
                LableDay=Label(fram3,text='')
                LableDay.place(x=250, y=20)
                if len(dateinf)>0:
                    LableDay.config(text='نوع روز مشخص شده ')
                    dateinff=dateinf[0]
                    Label(fram3, text=dateinff[0]).place(x=100, y=20)
                elif len(dateinf)==0:
                    LableDay.config(text='نوع روز')
                    dayType['values'] = (' روز کاری ', ' روز تعطیل با حقوق ', ' روز تعطیل بدون حقوق',)
                    dayType.current()
                    dayType.place(x=70, y=20)

                label.configure(text='تاریخ انتخابی:   ' + SelectedDate)
                B1.place(x=190, y=290)
                B1.config(command=lambda: submit(SelectedDate,dateinf))


    calendar = JCalendar(fram2, selectbackground='purple', selectforeground='white')
    calendar.place(x=5, y=20)
    Button(fram2, text='انتخاب', command=validate).place(x=200, y=205)
    label = Label(fram2)
    label.place(x=160, y=235)


    B1 = Button(fram2, text='تایید و ادامه', background='purple', fg='white')
    B1.place()