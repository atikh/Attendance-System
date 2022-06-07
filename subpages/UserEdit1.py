from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from subpages.DataBaseConnection import UserNames , getAllValues2 , userEdit


PersianChar = ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م',
               'ک', 'گ', 'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', ' ', 'ی', 'ي', 'ژ', 'آ']


def Registrationform():
    import tkinter as tk
    reg_screen = tk.Toplevel()
    reg_screen.title("فرم تغییرات کارمند")
    reg_screen.iconphoto(False, PhotoImage(file='images\\logos.png'))
    reg_screen.geometry("350x190")
    name = StringVar(reg_screen)
    fmlName = StringVar(reg_screen)
    contact = StringVar(reg_screen)
    gender = IntVar(reg_screen)
    ntnalCode = StringVar(reg_screen)
    state = StringVar(reg_screen)
    message = StringVar(reg_screen)
    reasonToDelete = StringVar(reg_screen)

    def reload():
        reg_screen.destroy()
        Registrationform()

    # Creating layout of Registration form
    Ltop = Label(reg_screen, width="300", text="لطفا کارمند مورد نظر را انتخاب نمایید", bg="purple", fg="white")
    Ltop.pack(anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.pack(anchor='n')


    new_image = ImageTk.PhotoImage((Image.open("images/logo farsi eng.png")).resize((160, 40), Image.ANTIALIAS))
    canvas.create_image(10, 10, anchor=NW, image=new_image)

    L2 = Label(reg_screen, text="نام کارمند ")
    L2.place(x=300, y=100, anchor='e')
    UserLists, idList = UserNames()
    data = UserLists
    cb = ttk.Combobox(reg_screen, values=data)
    cb.place(x=70, y=90)

    def choose():
        b = cb.current()
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

        if b == -1:
            MError.place(x=90, y=160)
        else:
            reg_screen.geometry("350x450")
            Ltop.config(text="لطفا تغییرات را وارد نمایید")
            B1.place(x=420)
            L1.place(x=420)
            cb.place(x=420)
            MError.place(x=420)
            personID, pname, pfmlName, pcontact, pgender, pntnalCode, EndHrs,EndHrs5= getAllValues2(idList,cb.current())

            Label(reg_screen, text="نام         * ").place(x=300, y=100, anchor='e')
            global txtFirstName
            txtFirstName = StringVar(reg_screen)
            entFirstName = Entry(reg_screen, textvariable=txtFirstName, highlightcolor='Purple', highlightthickness=1,
                                 justify='right')
            entFirstName.place(x=80, y=92)
            entFirstName.insert(0, pname)
            txtFirstName.trace('w', checkValidation)

            Label(reg_screen, text="نام خانوادگی * ").place(x=300, y=145, anchor='e')
            global txtLastName
            txtLastName = StringVar(reg_screen)
            entLastName = Entry(reg_screen, textvariable=txtLastName, highlightcolor='Purple', highlightthickness=1,
                                justify='right')
            entLastName.place(x=80, y=137)
            entLastName.insert(0, pfmlName)
            txtLastName.trace('w', checkValidation)

            Label(reg_screen, text="شماره تماس * ").place(x=300, y=189, anchor='e')
            global txtPhoneNumber
            txtPhoneNumber = StringVar(reg_screen)
            entPhoneNumber = Entry(reg_screen, textvariable=txtPhoneNumber, highlightcolor='Purple',
                                   highlightthickness=1)
            entPhoneNumber.place(x=80, y=181)
            entPhoneNumber.insert(0, pcontact)
            txtPhoneNumber.trace('w', checkValidation)

            Label(reg_screen, text="جنسیت * ").place(x=300, y=230, anchor='e')
            global gender
            gender = StringVar(reg_screen)
            Radiobutton(reg_screen, text="آقا", variable=gender, value="آقا", tristatevalue=0).place(x=80, y=220)
            Radiobutton(reg_screen, text="خانم", variable=gender, value="خانم", tristatevalue=0).place(x=140, y=220)
            Label(reg_screen, text="شماره ملی ").place(x=300, y=265, anchor='e')

            global txtNationalCode
            txtNationalCode = StringVar(reg_screen)
            entNationalCode = Entry(reg_screen, textvariable=txtNationalCode)
            entNationalCode.place(x=80, y=255)
            entNationalCode.insert(0, pntnalCode)
            txtNationalCode.trace('w', checkValidation)

            global entEndHourNormal
            Label(reg_screen, text="اتمام ساعت کاری * ").place(x=300, y=310, anchor='e')
            V1=('16', '17', '18', '19')
            entEndHourNormal = ttk.Combobox(reg_screen, values=V1, width=5, justify=RIGHT)
            indices =V1.index(str(EndHrs))
            entEndHourNormal.current(indices)
            entEndHourNormal.place(x=106, y=300)

            global entEndHour5
            Label(reg_screen, text="اتمام ساعت کاری پنجشنبه‌ * ").place(x=300, y=360, anchor='e')
            V2=('12', '13', '14', '15')
            entEndHour5 = ttk.Combobox(reg_screen, values=V2, width=5, justify=RIGHT)
            indice2 =V2.index(str(EndHrs5))
            entEndHour5.current(indice2)
            entEndHour5.place(x=106, y=350)

        LableSabt = Label(reg_screen, text="", fg='purple')
        LableSabt.place(x=400)

        def submitEdit(personID, LableSabt):
            FN = txtFirstName.get()
            LN = txtLastName.get()
            PH = txtPhoneNumber.get()
            Ge = gender.get()
            NT = txtNationalCode.get()
            EndN = entEndHourNormal.get()
            End5 = entEndHour5.get()
            if FN == '' or LN == '' or PH == '' or Ge == '':
                LableSabt.config(text="!!لطفا تمامی مقادیر ستاره‌دار را پر نمایید!!")
                LableSabt.place(x=70, y=420)
            elif len(PH) not in (11, 8):
                LableSabt.config(text="!! شماره تماس صحیح نیست !!")
                LableSabt.place(x=90, y=420)
            else:
                userEdit(FN, LN, PH, Ge, NT, EndN, End5, personID)
                L5 = Label(reg_screen, fg='purple', text="!! تغییرات با موفقیت ثبت گردید !!")
                L5.place(x=97, y=420)
                reg_screen.after(1000, lambda: reg_screen.destroy())



        Button(reg_screen, text="ذخیره تغییرات", width=10, height=1, bg="purple", fg="white",
               command=lambda: submitEdit(personID, LableSabt)) \
            .place(x=190, y=390)
        Button(reg_screen, text="لغو و بازگشت ", width=10, height=1, bg="purple", fg="white",
               command=lambda: reload()).place(x=90, y=390)

    MError = Message(reg_screen, text="!! لطفا فردی را انتخاب نمایید !!", width=200, fg='purple')
    MError.place(x=420)
    B1 = Button(reg_screen, text="انتخاب و ادامه", width=10, height=1, bg="purple", fg="white",
                command=lambda: choose())
    B1.place(x=130, y=130)
    reg_screen.mainloop()


