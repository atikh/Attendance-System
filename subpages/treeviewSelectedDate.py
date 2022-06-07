from tkinter import *
from tkinter import ttk

from subpages.DataBaseConnection import GetInfDay, UserNamesWithID

class MaintreeViewSelectedDay:

    def __init__(self):
        pass

    def Registrationform(self,Date):
        DbName = "DB/GolbargDonya.db"
        global reg_screen
        reg_screen = Tk()
        text = "گزارش در تاریخ : "+ str(Date[0])
        reg_screen.title(text)
        reg_screen.geometry("800x300")
        USERID, DayInformation = GetInfDay(Date[0])
        UserList=UserNamesWithID(USERID)


        scrollbary = Scrollbar(reg_screen, orient=VERTICAL)
        scrollbarx = Scrollbar(reg_screen, orient=HORIZONTAL)
        tree = ttk.Treeview(reg_screen, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9","10"),selectmode="extended", height=300,
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, style="mystyle.Treeview")
        style = ttk.Style()
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#c2c2c2')
        tree.tag_configure('Title', background='purple', foreground='white')
        tree.tag_configure('oddE', background='#E8E8E8')
        tree.tag_configure('evenE', background='#c2c2c2')

        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)


        tree.heading('10', text="نام و نام خانوادگی", anchor=E)
        tree.heading('9', text="تاریخ", anchor=E)
        tree.heading('8', text="نوع روز", anchor=E)
        tree.heading('7', text="وضعیت", anchor=E)
        tree.heading('6', text="تاخیر س", anchor=E)
        tree.heading('5', text="تاخیر د", anchor=E)
        tree.heading('4', text="مرخصی س", anchor=E)
        tree.heading('3', text="مرخصی د", anchor=E)
        tree.heading('2', text="اضافه‌کاری س", anchor=E)
        tree.heading('1', text="اضافه‌کاری د", anchor=E)


        tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=E)
        tree.column('#1', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#2', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#3', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#4', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#5', stretch=NO, minwidth=0, width=50, anchor=E)
        tree.column('#6', stretch=NO, minwidth=0, width=50, anchor=E)
        tree.column('#7', stretch=NO, minwidth=0, width=60, anchor=E)
        tree.column('#8', stretch=NO, minwidth=0, width=100, anchor=E)
        tree.column('#9', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#10', stretch=NO, minwidth=0, width=120, anchor=E)

        i=0
        j=0
        for data in DayInformation:
            if data[3] == 0:
                if i % 2 == 0:
                    tree.insert('', 'end', values=(data[9], data[8],data[7], data[6], data[5], data[4]," غایب", data[2], data[1], UserList[j]),
                                tags=('odd',))
                else:
                    tree.insert('', 'end', values=(data[9], data[8],data[7], data[6], data[5], data[4]," غایب", data[2], data[1], UserList[j]),
                                tags=('even',))
            else:

                if i % 2 == 0:
                    tree.insert('', 'end',
                                values=(data[9], data[8],data[7], data[6], data[5], data[4]," حاضر", data[2], data[1],UserList[j]),
                                tags=('odd',))
                else:
                    tree.insert('', 'end',
                                values=(data[9], data[8],data[7], data[6], data[5], data[4]," حاضر", data[2], data[1], UserList[j]),
                                tags=('even',))
            i += 1
            j += 1

        tree.pack()

        reg_screen.mainloop()
