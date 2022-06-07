from tkinter import *
from tkinter import ttk

class MaintreeViewTotal:

    def __init__(self):
        pass

    def Registrationform(self, idd, Year, Month, UserS):
        DbName = "DB/GolbargDonya.db"
        from subpages.DataBaseConnection import GetDateForTreeView

        global reg_screen
        reg_screen = Tk()
        text = "گزارش کلی ماهانه : " + UserS
        reg_screen.title(text)
        reg_screen.geometry("650x300")
        DayInformation = GetDateForTreeView(idd, Year, Month)

        tree = ttk.Treeview(reg_screen, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9",), selectmode="extended",
                            height=300,
                            style="mystyle.Treeview", show="tree")
        style = ttk.Style()
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#c2c2c2')
        tree.tag_configure('Title', background='purple', foreground='white')
        tree.tag_configure('oddE', background='#E8E8E8')
        tree.tag_configure('evenE', background='#c2c2c2')

        tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=E)
        tree.column('#1', stretch=NO, minwidth=0, width=20, anchor=E)
        tree.column('#2', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#3', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#4', stretch=NO, minwidth=0, width=80, anchor=E)
        tree.column('#5', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#6', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#7', stretch=NO, minwidth=0, width=70, anchor=E)
        tree.column('#8', stretch=NO, minwidth=0, width=120, anchor=E)
        tree.column('#9', stretch=NO, minwidth=0, width=20, anchor=E)
        CountDay = 0
        # variable for rooze kari
        SumTakhirH = 0
        SumTakhirM = 0
        SumMorakhasiH = 0
        SumMorakhasiM = 0
        SumEzafeH = 0
        SumEzafeM = 0
        RoozeKari = 0
        RoozeTBaH = 0
        RoozeTBiH = 0

        # variable for rooze t bi H
        SumTakhirHBiH = 0
        SumTakhirMBiH = 0
        SumMorakhasiHBiH = 0
        SumMorakhasiMBiH = 0
        SumEzafeHBiH = 0
        SumEzafeMBiH = 0
        # variable for rooze t ba H
        SumTakhirHBaH = 0
        SumTakhirMBaH = 0
        SumMorakhasiHBaH = 0
        SumMorakhasiMBaH = 0
        SumEzafeHBaH = 0
        SumEzafeMBaH = 0

        i = 0
        for data in DayInformation:
            if not data[2] == 0:
                CountDay += 1
                if data[1] == ' روز کاری ':
                    RoozeKari += 1
                    SumTakhirH += data[3]
                    SumTakhirM += data[4]
                    SumMorakhasiH += data[5]
                    SumMorakhasiM += data[6]
                    SumEzafeH += data[7]
                    SumEzafeM += data[8]
                elif data[1] == ' روز تعطیل با حقوق ':
                    RoozeTBaH += 1
                    SumTakhirHBaH += data[3]
                    SumTakhirMBaH += data[4]
                    SumMorakhasiHBaH += data[5]
                    SumMorakhasiMBaH += data[6]
                    SumEzafeHBaH += data[7]
                    SumEzafeMBaH += data[8]
                elif data[1] == ' روز تعطیل بدون حقوق':
                    RoozeTBiH += 1
                    SumTakhirHBiH += data[3]
                    SumTakhirMBiH += data[4]
                    SumMorakhasiHBiH += data[5]
                    SumMorakhasiMBiH += data[6]
                    SumEzafeHBiH += data[7]
                    SumEzafeMBiH += data[8]

            i += 1

        SumTakhirH += (SumTakhirM // 60)
        SumTakhirM = SumTakhirM % 60
        SumMorakhasiH += (SumMorakhasiM // 60)
        SumMorakhasiM = SumMorakhasiM % 60
        SumEzafeH += (SumEzafeM // 60)
        SumEzafeM = SumEzafeM % 60

        # tatil ba hoghoogh
        SumTakhirHBaH += (SumTakhirMBaH // 60)
        SumTakhirMBaH = SumTakhirMBaH % 60
        SumMorakhasiHBaH += (SumMorakhasiMBaH // 60)
        SumMorakhasiMBaH = SumMorakhasiMBaH % 60
        SumEzafeHBaH += (SumEzafeMBaH // 60)
        SumEzafeMBaH = SumEzafeMBaH % 60

        # tatil bedoone hoghoogh
        SumTakhirHBiH += (SumTakhirMBiH // 60)
        SumTakhirMBiH = SumTakhirMBiH % 60
        SumMorakhasiHBiH += (SumMorakhasiMBiH // 60)
        SumMorakhasiMBiH = SumMorakhasiMBiH % 60
        SumEzafeHBiH += (SumEzafeMBiH // 60)
        SumEzafeMBiH = SumEzafeMBiH % 60

        tree.insert('', 'end', values=('', '', '', 'غیاب', ' حضور و ', 'اطلاعات', '', '', '**'), tags=('Title',))
        tree.insert('', 'end', values=(
        RoozeTBiH, 'تعطیل بی ح', RoozeTBaH, 'تعطیل با ح', RoozeKari, ' روز کاری', CountDay, 'مجموع روزهای حاضر', '**'),
                    tags=('oddE',))
        ### Rooze kari
        tree.insert('', 'end', values=('', '', '', 'کاری', ' روز  ', 'اطلاعات', '', '', '**'), tags=('Title',))
        tree.insert('', 'end', values=('', '', '', 'دقیقه', SumTakhirM, 'ساعت و', SumTakhirH, 'مجموع تاخیرها', '**'),
                    tags=('evenE',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumMorakhasiM, 'ساعت و', SumMorakhasiH, 'مجموع مرخصی‌ها', '**'),
                    tags=('oddE',))
        tree.insert('', 'end', values=('', '', '', 'دقیقه', SumEzafeM, 'ساعت و', SumEzafeH, 'مجموع اضافه‌کاری', '**'),
                    tags=('evenE',))

        #### rooze tatile ba hoghoogh
        tree.insert('', 'end', values=('', '', 'با حقوق', 'تعطیل ', ' روز  ', 'اطلاعات', '', '', '**'), tags=('Title',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumTakhirMBaH, 'ساعت و', SumTakhirHBaH, 'مجموع تاخیرها', '**'),
                    tags=('evenE',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumMorakhasiMBaH, 'ساعت و', SumMorakhasiHBaH, 'مجموع مرخصی‌ها', '**'),
                    tags=('oddE',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumEzafeMBaH, 'ساعت و', SumEzafeHBaH, 'مجموع اضافه‌کاری', '**'),
                    tags=('evenE',))

        #### rooze tatile bedoone hoghoogh
        tree.insert('', 'end', values=('', '', 'بدون حقوق', 'تعطیل ', ' روز  ', 'اطلاعات', '', '', '**'),
                    tags=('Title',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumTakhirMBiH, 'ساعت و', SumTakhirHBiH, 'مجموع تاخیرها', '**'),
                    tags=('evenE',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumMorakhasiMBiH, 'ساعت و', SumMorakhasiHBiH, 'مجموع مرخصی‌ها', '**'),
                    tags=('oddE',))
        tree.insert('', 'end',
                    values=('', '', '', 'دقیقه', SumEzafeMBiH, 'ساعت و', SumEzafeHBiH, 'مجموع اضافه‌کاری', '**'),
                    tags=('evenE',))

        tree.pack()

        reg_screen.mainloop()
