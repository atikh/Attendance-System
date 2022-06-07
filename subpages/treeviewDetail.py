from tkinter import *
from tkinter import ttk

class MaintreeViewDetail:

    def __init__(self):
        pass

    def Registrationform(self, id, Year, Month, UserS):
        DbName = "DB/GolbargDonya.db"
        from subpages.DataBaseConnection import GetDateForTreeView

        global reg_screen
        reg_screen = Tk()

        text = "جزيبات اطلاعات ماهانه : " + UserS
        reg_screen.title(text)
        reg_screen.geometry("850x300")

        DayInformation = GetDateForTreeView(id, Year, Month)

        scrollbary = Scrollbar(reg_screen, orient=VERTICAL)
        scrollbarx = Scrollbar(reg_screen, orient=HORIZONTAL)
        tree = ttk.Treeview(reg_screen, columns=(
        "اضافه‌کاری دقیقه", "اضافه‌کاری ساعت", "مرخصی دقیقه", "مرخصی ساعت", "تاخیر دقیقه", "تاخیر ساعت", "وضعیت",
        "نوع روز", "تاریخ"), selectmode="extended", height=300,
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

        tree.heading('تاریخ', text="تاریخ", anchor=E)
        tree.heading('نوع روز', text="نوع روز", anchor=E)
        tree.heading('وضعیت', text="وضعیت", anchor=E)
        tree.heading('تاخیر ساعت', text="تاخیر ساعت", anchor=E)
        tree.heading('تاخیر دقیقه', text="تاخیر دقیقه", anchor=E)
        tree.heading('مرخصی ساعت', text="مرخصی ساعت", anchor=E)
        tree.heading('مرخصی دقیقه', text="مرخصی دقیقه", anchor=E)
        tree.heading('اضافه‌کاری ساعت', text="اضافه‌کاری ساعت", anchor=E)
        tree.heading('اضافه‌کاری دقیقه', text="اضافه‌کاری دقیقه", anchor=E)
        tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=E)
        tree.column('#1', stretch=NO, minwidth=0, width=100, anchor=E)
        tree.column('#2', stretch=NO, minwidth=0, width=100, anchor=E)
        tree.column('#3', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#4', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#5', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#6', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#7', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#8', stretch=NO, minwidth=0, width=120, anchor=E)
        tree.column('#9', stretch=NO, minwidth=0, width=60, anchor=E)

        i = 0
        for data in DayInformation:
            if data[2] == 0:
                if i % 2 == 0:
                    tree.insert('', 'end', values=('-', '-', '-', '-', '-', '-', 'غایب', data[1], data[0]),
                                tags=('odd',))
                else:
                    tree.insert('', 'end', values=('-', '-', '-', '-', '-', '-', 'غایب', data[1], data[0]),
                                tags=('even',))
            else:

                if i % 2 == 0:
                    tree.insert('', 'end',
                                values=(data[8], data[7], data[6], data[5], data[4], data[3], 'حاضر', data[1], data[0]),
                                tags=('odd',))
                else:
                    tree.insert('', 'end',
                                values=(data[8], data[7], data[6], data[5], data[4], data[3], 'حاضر', data[1], data[0]),
                                tags=('even',))
            i += 1

        tree.pack()

        reg_screen.mainloop()
