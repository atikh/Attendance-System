from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from subpages.DataBaseConnection import UserNames ,delete




def Registrationform():
    import tkinter as tk
    reg_screen = tk.Toplevel()
    reg_screen.title("فرم حذف کارمند")
    reg_screen.iconphoto(False, PhotoImage(file='images\\logos.png'))
    reg_screen.geometry("350x230")
    reasonToDelete = StringVar(reg_screen)

    def cancel():
        reg_screen.destroy()

    def Deletee():
        if reasonToDelete.get() == '':
            L1 = Label(reg_screen, fg='purple', text="!! لطفا علت را بنویسید!!")
            L1.place(x=100, y=205)
        else:
            R = reasonToDelete.get()
            b = idList[cb.current()]
            delete(R, b[0])
            L2 = Label(reg_screen, fg='purple', text="!! کارمند با موفقیت حذف گردید !!")
            L2.place(x=97, y=205)
            reg_screen.after(1000, lambda: reg_screen.destroy())

    # Creating layout of Registration form
    Label(reg_screen, width="300", text="لطفا کارمند مورد نظر را انتخاب نمایید", bg="purple", fg="white").pack(
        anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.pack(anchor='n')
    new_image = ImageTk.PhotoImage((Image.open("images/logo farsi eng.png")).resize((160, 40), Image.ANTIALIAS))
    canvas.create_image(10, 10, anchor=NW, image=new_image)

    Label(reg_screen, text="نام کارمند ").place(x=300, y=100, anchor='e')
    UserLists, idList = UserNames()
    data = UserLists
    cb = ttk.Combobox(reg_screen, values=data)
    cb.place(x=70, y=90)
    Label(reg_screen, text="علت حذف ").place(x=300, y=140, anchor='e')
    Entry(reg_screen, textvariable=reasonToDelete, width=30).place(x=30, y=135)

    Button(reg_screen, text="حذف کارمند", width=10, height=1, bg="purple", fg="white",
           command=lambda: Deletee()).place( x=190, y=175)
    Button(reg_screen, text="لغو و بازگشت", width=10, height=1, bg="purple", fg="white", command=cancel).place(x=80,
                                                                                                               y=175)
    reg_screen.mainloop()


