import sqlite3

DbName = "DB/GolbargDonya.db"


def GetDateForTreeView(ID, Year, Month):
    conn = sqlite3.connect(DbName)
    m = str(Month)
    if len(m) == 1:
        m = '0' + m
    LikeMonth = '%/' + m + '/' + str(Year)
    values = (ID[0], LikeMonth)
    DayInformation = conn.cursor().execute("SELECT Datee, DayType, YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM,"
                                           " EzafekariH, EzafekariM FROM Date WHERE PersonID=? AND Datee LIKE ? ",
                                           values).fetchall()

    conn.commit()
    return DayInformation

def DeleteUserNames():

    conn = sqlite3.connect(DbName)
    l_name = conn.cursor().execute("SELECT LastName FROM Person WHERE EXIST=0").fetchall()
    f_name = conn.cursor().execute("SELECT FirstName FROM Person WHERE EXIST=0").fetchall()
    id_ = conn.cursor().execute("SELECT ID FROM Person WHERE EXIST=0").fetchall()
    UserList = []
    namelist = []
    familyname = []
    idList = []
    for name, surname, idd in zip(f_name, l_name, id_):
        UserList.append(name + surname)
        namelist.append(name)
        familyname.append(surname)
        idList.append(idd)
    conn.commit()
    return UserList, idList


def UserNames():
    conn = sqlite3.connect(DbName)
    l_name = conn.cursor().execute("SELECT LastName FROM Person WHERE EXIST=1").fetchall()
    f_name = conn.cursor().execute("SELECT FirstName FROM Person WHERE EXIST=1").fetchall()
    id_ = conn.cursor().execute("SELECT ID FROM Person WHERE EXIST=1").fetchall()
    UserList = []
    namelist = []
    familyname = []
    idList = []
    for name, surname, idd in zip(f_name, l_name, id_):
        UserList.append(name + surname)
        namelist.append(name)
        familyname.append(surname)
        idList.append(idd)
    conn.commit()
    return UserList, idList

def delete(R,b):
    query = ' UPDATE Person SET Exist = ? ,DeleteReason=? WHERE ID=?'
    Valuse = (0, R,b)
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Valuse)
        connection.commit()
def userdef(FN, LN, PH, Ge, NT, EndN, End5):

    query = "INSERT INTO Person (FirstName,LastName ,PhoneNumber,Gender,NationalCode,Exist,EndH,EndH5) Values(?,?,?,?,?,?,?,?)"
    Params = (FN, LN, PH, Ge, NT, 1, EndN, End5)
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Params)
        connection.commit()

def userEdit(FN, LN, PH, Ge, NT, EndN, End5, personID):
    query = ' UPDATE Person SET FirstName = ?,LastName = ? ,PhoneNumber = ?,Gender = ?,NationalCode = ? ,EndH = ?,' \
            'EndH5 = ? WHERE ID=?'
    Valuse = (FN, LN, PH, Ge, NT, EndN, End5, personID)
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Valuse)
        connection.commit()

def Recovery(b):
    query = ' UPDATE Person SET Exist = ? ,DeleteReason=? WHERE ID=?'
    Valuse = (1, 0, b[0])
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Valuse)
        connection.commit()

def getAllValues(idList, cbCurrent, Dat):
    b = idList[cbCurrent]
    query = "SELECT DayType, YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM, EzafekariH, EzafekariM ,ID FROM Date WHERE PersonID= ? AND Datee=?"
    Valuse = (b[0], Dat)
    conn = sqlite3.connect(DbName)
    ExtractedItems = conn.cursor().execute(query, Valuse).fetchall()
    conn.commit()
    ExtractedItems = ExtractedItems[0]
    DayType = ExtractedItems[0]
    YN = ExtractedItems[1]
    TakhirH = ExtractedItems[2]
    TakhirM = ExtractedItems[3]
    MorakhasiH = ExtractedItems[4]
    MorakhasiM = ExtractedItems[5]
    EzafekariH = ExtractedItems[6]
    EzafekariM = ExtractedItems[7]
    IDDate = ExtractedItems[8]
    conn.commit()
    return DayType, YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM, EzafekariH, EzafekariM, IDDate


def UserNamesHozoorGhiab(Dat):
    conn = sqlite3.connect(DbName)
    PERSONIDSETS = conn.cursor().execute("SELECT PersonID FROM Date WHERE Datee=?", (Dat[0],)).fetchall()
    l_name = conn.cursor().execute("SELECT LastName FROM Person WHERE Exist=1").fetchall()
    f_name = conn.cursor().execute("SELECT FirstName FROM Person WHERE Exist=1").fetchall()
    id_ = conn.cursor().execute("SELECT ID FROM Person WHERE Exist=1").fetchall()
    UserList = []
    namelist = []
    familyname = []
    idList = []
    for name, surname, idd in zip(f_name, l_name, id_):
        if idd not in PERSONIDSETS:
            UserList.append(name + surname)
            namelist.append(name)
            familyname.append(surname)
            idList.append(idd)
    conn.commit()
    return UserList, idList


def getAllValues2(idList, cbCurrent):
    b = (idList[cbCurrent])
    id_sql = tuple(b)
    conn = sqlite3.connect(DbName)
    id, name, fmlName, contact, gender, ntnalCode, EndHrs, EndHrs5 = \
        conn.cursor().execute("SELECT ID, FirstName,LastName ,PhoneNumber,Gender,NationalCode,EndH ,EndH5 "
                              " FROM Person WHERE ID= ?", id_sql).fetchall()[0]
    conn.commit()
    return id, name, fmlName, contact, gender, ntnalCode, EndHrs, EndHrs5

def GetInfDay(Date):
    conn = sqlite3.connect(DbName)
    Date=(Date,)
    USERID=conn.cursor().execute("SELECT PersonID FROM Date WHERE Datee = ? ",Date).fetchall()
    PersonsDayInformation = conn.cursor().execute("SELECT PersonID , Datee, DayType, YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM,"
                                           " EzafekariH, EzafekariM FROM Date WHERE Datee = ? ",Date).fetchall()
    conn.commit()
    return USERID, PersonsDayInformation

def UserNamesWithID(USERID):
    conn = sqlite3.connect(DbName)
    USER = []
    for i in range (0, len(USERID)):
        ID=USERID[i]
        l_name = conn.cursor().execute("SELECT LastName FROM Person WHERE ID = ? ",ID).fetchall()
        f_name = conn.cursor().execute("SELECT FirstName FROM Person WHERE ID = ? ",ID).fetchall()
        for name, surname in zip(f_name, l_name):
            USER.append(name + surname)
        conn.commit()
    return USER


def findDate(date):
    date=(date,)
    conn = sqlite3.connect(DbName)
    dateinf=conn.cursor().execute("SELECT DayType FROM Date WHERE Datee = ? ",date).fetchall()
    conn.commit()
    return dateinf

def updateDayType(date,Daytype):
    Par=(Daytype,date)
    conn = sqlite3.connect(DbName)
    conn.cursor().execute(' UPDATE Date SET DayType = ? WHERE Datee = ? ',Par).fetchall()
    conn.commit()

def sabtHozoor(Dat,idP,takhH, takhM, MorH, MorM, EzfH, EzfM):
    query = "INSERT OR IGNORE INTO Date (PersonID, Datee, DayType ,YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM, EzafekariH, EzafekariM)" \
            " Values(?,?,?,?,?,?,?,?,?,?)"
    Dat1 = Dat[0]
    DayT = Dat[1]
    Params = (idP, Dat1, DayT, 1, takhH, takhM, MorH, MorM, EzfH, EzfM)
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Params)
        connection.commit()

def sabtGhayeb(Dat,idP):
    query = "INSERT OR IGNORE INTO Date (PersonID, Datee, DayType ,YN, TakhirH, TakhirM, MorakhasiH, MorakhasiM, EzafekariH, EzafekariM)" \
            " Values(?,?,?,?,?,?,?,?,?,?)"
    Dat1 = Dat[0]
    DayT = Dat[1]
    Params = (idP, Dat1, DayT, 0, 0, 0, 0, 0, 0, 0)
    with sqlite3.connect(DbName) as connection:
        cursor = connection.cursor()
        cursor.execute(query, Params)
        connection.commit()