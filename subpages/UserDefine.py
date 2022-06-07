from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
from subpages.DataBaseConnection import userdef


PersianChar = ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م',
               'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', ' ', 'ی', 'ي', 'ژ', 'آ']

global reg_screen



def Registrationform():
    import tkinter as tk
    reg_screen = tk.Toplevel()
    reg_screen.title("فرم ایجاد کارمند")
    reg_screen.iconphoto(False, PhotoImage(file='images\\logos.png'))
    reg_screen.geometry("350x450")

    def cancel():
        reg_screen.destroy()

    # Creating layout of Registration form
    Label(reg_screen, width="300", text="لطفا اطلاعات زیر را تکمیل نمایید", bg="purple", fg="white").pack(anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.pack(anchor='n')
    new_image = ImageTk.PhotoImage((Image.open("images/logo farsi eng.png")).resize((160, 40), Image.ANTIALIAS))
    canvas.create_image(10, 10, anchor=NW, image=new_image)

    L1 = Label(reg_screen, fg='purple')

    def CheckPersian(TEXT, n):
        a = 0
        if len(TEXT.get()) > 0:
            if TEXT.get()[-1].upper() not in PersianChar:
                TEXT.set(TEXT.get()[:len(TEXT.get()) - 1])
                L1.place(x=60, y=n)
                L1.config(text="!! لطفا  مقدار فارسی وارد نمایید !!")
                a = 1
        return a

    def checkValidation(*args):
        a1 = CheckPersian(txtFirstName, 115)
        a2 = CheckPersian(txtLastName, 160)
        a3 = 0

        if len(txtFirstName.get()) > 15:
            txtFirstName.set(txtFirstName.get()[:len(txtFirstName.get()) - 1])
        elif len(entFirstName.get()) > 2:
            entFirstName.config(highlightcolor='black')

        if len(txtLastName.get()) > 15:
            txtLastName.set(txtLastName.get()[:len(txtLastName.get()) - 1])
        if len(entLastName.get()) > 2:
            entLastName.config(highlightcolor='black')

        if len(entPhoneNumber.get()) > 11:
            txtPhoneNumber.set(txtPhoneNumber.get()[:len(txtPhoneNumber.get()) - 1])

        if len(entPhoneNumber.get()) >= 11:
            entPhoneNumber.config(highlightcolor='black')

        if not entPhoneNumber.get().isnumeric() and len(entPhoneNumber.get()) >= 1:
            txtPhoneNumber.set(txtPhoneNumber.get()[:len(txtPhoneNumber.get()) - 1])
            L1.config(text="!! لطفا  مقدار عددی وارد نمایید !!")
            L1.place(x=60, y=200)
            a3 = 1

        if not entNationalCode.get().isnumeric() and len(entNationalCode.get()) >= 1:
            txtNationalCode.set(txtNationalCode.get()[:len(txtNationalCode.get()) - 1])
            L1.config(text="!! لطفا  مقدار عددی وارد نمایید !!")
            L1.place(x=60, y=272)

        if len(entNationalCode.get()) > 10:
            txtNationalCode.set(txtNationalCode.get()[:len(txtNationalCode.get()) - 1])
            L1.config(text="!! کدملی ۱۰ رقمی است !!")
            L1.place(x=60, y=272)

        elif a1 == 0 and a2 == 0 and a3 == 0:
            L1.place(x=600)

        # فرم

    Label(reg_screen, text="نام * ").place(x=300, y=100, anchor='e')
    global txtFirstName
    txtFirstName = StringVar(reg_screen)
    txtFirstName.trace('w', checkValidation)
    entFirstName = Entry(reg_screen, textvariable=txtFirstName, highlightcolor='Purple', highlightthickness=1,
                         justify='right')
    entFirstName.place(x=80, y=92)

    Label(reg_screen, text="نام خانوادگی * ").place(x=300, y=145, anchor='e')
    global txtLastName
    txtLastName = StringVar(reg_screen)
    entLastName = Entry(reg_screen, textvariable=txtLastName, highlightcolor='Purple', highlightthickness=1,
                        justify='right')
    entLastName.place(x=80, y=137)
    txtLastName.trace('w', checkValidation)

    Label(reg_screen, text="شماره تماس * ").place(x=300, y=189, anchor='e')
    global txtPhoneNumber
    txtPhoneNumber = StringVar(reg_screen)
    txtPhoneNumber.trace('w', checkValidation)
    entPhoneNumber = Entry(reg_screen, textvariable=txtPhoneNumber, highlightcolor='Purple', highlightthickness=1)
    entPhoneNumber.place(x=80, y=181)

    Label(reg_screen, text="جنسیت * ").place(x=300, y=230, anchor='e')
    global gender
    gender = StringVar(reg_screen)
    Radiobutton(reg_screen, text="آقا", variable=gender, value="آقا", tristatevalue=0).place(x=80, y=220)
    Radiobutton(reg_screen, text="خانم", variable=gender, value="خانم", tristatevalue=0).place(x=140, y=220)

    Label(reg_screen, text="شماره ملی ").place(x=300, y=265, anchor='e')
    global txtNationalCode
    txtNationalCode = StringVar(reg_screen)
    txtNationalCode.trace('w', checkValidation)
    entNationalCode = Entry(reg_screen, textvariable=txtNationalCode)
    entNationalCode.place(x=80, y=255)

    global entEndHourNormal
    Label(reg_screen, text="اتمام ساعت کاری * ").place(x=300, y=310, anchor='e')
    entEndHourNormal = ttk.Combobox(reg_screen, values=('16', '17', '18', '19'), width=5, justify=RIGHT)
    entEndHourNormal.place(x=106, y=300)

    global entEndHour5
    Label(reg_screen, text="اتمام ساعت کاری پنجشنبه‌ * ").place(x=300, y=360, anchor='e')
    entEndHour5 = ttk.Combobox(reg_screen, values=('12', '13', '14', '15'), width=5, justify=RIGHT)
    entEndHour5.place(x=106, y=350)

    LableSabt = Label(reg_screen, text="", fg='purple')
    LableSabt.place(x=400)

    def register(LableSabt):
        # getting form data
        FN = txtFirstName.get()
        LN = txtLastName.get()
        PH = txtPhoneNumber.get()
        Ge = gender.get()
        NT = txtNationalCode.get()
        EndN = entEndHourNormal.get()
        End5 = entEndHour5.get()
        if FN == '' or LN == '' or PH == '' or Ge == '' or EndN == '' or len(End5) == 0:
            LableSabt.config(text="!!لطفا تمامی مقادیر ستاره‌دار را پر نمایید!!")
            LableSabt.place(x=70, y=420)
        elif len(PH) not in (11, 8):
            LableSabt.config(text="!! شماره تماس صحیح نیست !!")
            LableSabt.place(x=90, y=420)

        else:
            userdef(FN, LN, PH, Ge, NT, EndN, End5)
            LableSabt.config(text="اطلاعات با موفقیت ثبت گردید")
            LableSabt.place(x=90, y=420)
            reg_screen.after(1000, lambda: reg_screen.destroy())

    Button(reg_screen, text="ثبت کاربر", width=10, height=1, bg="purple", fg="white",
           command=lambda: register(LableSabt)).place(x=190,
                                                      y=390)
    Button(reg_screen, text="لغو و بازگشت", width=10, height=1, bg="purple", fg="white", command=cancel).place(x=80,
                                                                                                               y=390)
    reg_screen.mainloop()
