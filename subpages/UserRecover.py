from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from subpages.DataBaseConnection import DeleteUserNames, Recovery


def Registrationform():
    import tkinter as tk
    reg_screen = tk.Toplevel()
    reg_screen.title("فرم بازگرداندن کارمند")
    reg_screen.iconphoto(False, PhotoImage(file='images\\logos.png'))
    reg_screen.geometry("350x180")

    def cancel():
        reg_screen.destroy()

    # Creating layout of Registration form
    Label(reg_screen, width="300", text="لطفا کارمند مورد نظر را انتخاب نمایید", bg="purple", fg="white").pack(
        anchor='e')
    canvas = Canvas(reg_screen, width=160, height=45)
    canvas.pack(anchor='n')
    new_image = ImageTk.PhotoImage((Image.open("images/logo farsi eng.png")).resize((160, 40), Image.ANTIALIAS))
    canvas.create_image(10, 10, anchor=NW, image=new_image)

    Label(reg_screen, text="نام کارمند حذف شده").place(x=310, y=100, anchor='e')
    UserLists, idList = DeleteUserNames()

    if not len(UserLists) == 0:
        def recovery():
            b = idList[cb.current()]
            Recovery(b)
            L2 = Label(reg_screen, fg='purple', text="!! کارمند با موفقیت بازگردانده شد !!")
            L2.place(x=88, y=157)
            reg_screen.after(1000, lambda: reg_screen.destroy())

    data = UserLists
    cb = ttk.Combobox(reg_screen, values=data)
    cb.place(x=50, y=90)
    if len(UserLists) > 1:
        Button(reg_screen, text="بازگرداندن کارمند", width=15, height=1, bg="purple", fg="white",
               command=lambda: recovery()).place(x=180, y=130)

    Bazgasht = Button(reg_screen, text="لغو و بازگشت", width=15, height=1, bg="purple", fg="white", command=cancel)
    Bazgasht.place(x=50, y=130)
    reg_screen.mainloop()
