
from tkinter import *
import tkinter as tk
import os
current_directory = os.getcwd()


def MenueModiriatProfile(reg_screen):

    fram2 = tk.Frame(reg_screen, width=450, height=340, relief=SUNKEN, borderwidth=1)
    fram2.place(x=150, y=40)

    # # MENUE 1  مدیریت پروفایل ها
    # # MENUE 1  مدیریت پروفایل ها
    def userDef():
        from subpages.UserDefine import Registrationform
        Registrationform()
    def userDel():
        from subpages.UserDelete import Registrationform
        Registrationform()
    def userEdit():
        from subpages.UserEdit1 import Registrationform
        Registrationform()
    def userRet():
        from subpages.UserRecover import Registrationform
        Registrationform()


    Bsabtkarbar = Button(fram2, text=' ثبت کارمند جدید', command=lambda: userDef(),
                         width="17", bg='white',
                         fg='black')
    Bsabtkarbar.place(x=280, y=30, anchor='e')
    Bsabtkarbar = Button(fram2, text=' حذف کارمند از لیست', command=lambda: userDel(),
                         width="17", bg='white',
                         fg='black')
    Bsabtkarbar.place(x=280, y=70, anchor='e')
    Bsabtkarbar = Button(fram2, text=' تغییرات در اطلاعات', command=lambda: userEdit(),
                         width="17", bg='white',
                         fg='black')
    Bsabtkarbar.place(x=280, y=110, anchor='e')

    Bsabtkarbar = Button(fram2, text=' بازگردانی کاربر', command=lambda: userRet(),
                         width="17", bg='white',
                         fg='black')
    Bsabtkarbar.place(x=280, y=150, anchor='e')
