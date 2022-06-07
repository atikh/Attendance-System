from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk



def Registrationform():
    global reg_screen
    reg_screen = Tk()
    reg_screen.title("فرم حضور غیاب گلبرگ دنیا")
    reg_screen.iconphoto(False, PhotoImage(file='images/logos.png'))
    reg_screen.geometry("600x380")

    fram1 = tk.Frame(reg_screen, width=150, height=340, relief=SUNKEN,borderwidth=1)
    fram1.place(x=0,y=40)

    # TOP RIBBON
    Label(reg_screen, width="300", text=" سلام، روز خوش! لطفا منوی مورد نظر را انتخاب نمایید ", bg="purple", fg="white").pack(anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.place(x=-15,y=45)
    new_image = ImageTk.PhotoImage((Image.open("images/logo farsi eng.png")).resize((160, 40), Image.ANTIALIAS))
    canvas.create_image(10, 10, anchor=NW, image=new_image)



    fram2 = tk.Frame(reg_screen, width=450, height=340, relief=SUNKEN, borderwidth=1)
    fram2.place(x=150, y=40)
    canvas2 = Canvas(fram2, width=450, height=340)
    canvas2.place(x=0,y=0)
    new_image2 = ImageTk.PhotoImage((Image.open("images/Back1.png")).resize((450, 340), Image.ANTIALIAS))
    canvas2.create_image(1, 1, anchor=NW, image=new_image2)

    ###MENUE  hozoor ghiab
    def clickon0():
        B1.config(fg='White', bg='Purple')
        B2.config(fg='black', bg='White')
        B3.config(fg='black', bg='White')
        fram2 = tk.Frame(reg_screen, width=0, height=0)
        for widgets in fram2.winfo_children():
            widgets.destroy()
        import subpages.MenueSelectDate
        subpages.MenueSelectDate.menueSelectDate(reg_screen)
      # کلیک روی مدیریت پروفایل ها
    def clickon1():
        B1.config(fg='black', bg='White')
        B2.config(fg='White', bg='Purple')
        B3.config(fg='black', bg='White')
        fram2 = tk.Frame(reg_screen, width=0, height=0)
        for widgets in fram2.winfo_children():
            widgets.destroy()
        import subpages.MenueModidateProfile
        subpages.MenueModidateProfile.MenueModiriatProfile(reg_screen)

    # کلیک روی بررسی وضعیت کارمندان
    def clickon2():
        B1.config(fg='black', bg='White')
        B2.config(fg='black', bg='White')
        B3.config(fg='White', bg='Purple')
        fram2 = tk.Frame(reg_screen, width=0, height=0)
        for widgets in fram2.winfo_children():
            widgets.destroy()
        import subpages.MenueBarresiVaziat
        subpages.MenueBarresiVaziat.MenueVaziateKarmand(reg_screen)


    # ERROR

    B1 = Button(reg_screen, text=' لیست حضور و غیاب', command=lambda: clickon0(), width="17", bg='white',
                fg='black')
    B1.place(x=10, y=130)
    B2 = Button(reg_screen, text='مدیریت پروفایل ها', command=lambda: clickon1(), bg='white', fg='black',
                width="17")
    B2.place(x=10, y=170)
    B3 = Button(reg_screen, text='بررسی وضعیت کارمندان ', command=lambda: clickon2(), bg='white', fg='black',
                width="17")
    B3.place(x=10, y=210)

    reg_screen.mainloop()


Registrationform()
