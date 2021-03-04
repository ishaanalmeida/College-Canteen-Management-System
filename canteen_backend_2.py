import sqlite3
#canteen_backend
option=["NONE",
         "CHINESE DOSA","RAWA MASALA DOSA","CHOPSUEY DOSA","SADA DOSA",
         "VEG FRANKIE","PANEER FRANKIE","CHEESE FRANKIE","SCHEZWAN FRANKIE",
         "CHEESE SANDWICH","CHEESE CHILLI TOAST","VEG CLUB SANDWICH","GRILLED SANDWICH",
         "BHEL PURI","SEV PURI","DAHI PAPDI CHAAT","SAMOSA BHEL","RAGDA PURI",
         "PAV BHAJI","TAWA PULAO","MATAR PULAO","PANEER TIKKA BIRYANI",
         "PANEER TIKKA MASALA","PANEER SHAHI KORMA","PANEER TADKA",
         "PANEER GARLIC","VEG CRISPY","MANCHURIAN DRY","BUTTER NAAN","GARLIC NAAN","ROTI",
         "METHI PARATHA","PANEER PARATHA","ALOO PARATHA",
         "FRUIT SALAD","KHICHIYAMASALA PAPAD","BANANA MILKSHAKE","CHIKOO MILKSHAKE",
         "OREO SHAKE","LASSI","BUTTER MILK",
         "ORANGE JUICE","FRESH LIME JUICE","PINEAPPLE JUICE","TEA","COFFEE"]

def studentData():
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student2 (id INTEGER PRIMARY KEY,SAPID text, username text, stream text, year text, passowrd text)")
    cur.execute("CREATE TABLE IF NOT EXISTS countitem (password text,countt INTEGER)")
    for i in option:
        cur.execute("INSERT INTO countitem VALUES(?,?)",(i,0))
    con.commit()
    con.close()

def addStdRec(SAPID,username,stream,year,password,count):
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("INSERT INTO student2 VALUES(NULL,?,?,?,?,?)",(SAPID,username,stream,year,password))
    
    cur.execute(" SELECT countt FROM countitem WHERE password=?",(password,))
    cunt=0
    for i in cur.fetchone():
        cunt=i
    print(cunt)
    count=cunt+count
    cur.execute("UPDATE countitem set countt=? where password=?",(count,password,))               
    print("counting")
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student2")
    rows=cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student2 WHERE id=?",(id,))
    #cur.execute("UPDATE countitem set count=? where password=(select password from student2 WHERE id=?)",(count-1,id,))
    con.commit()
    con.close()

def searchData(SAPID=" ",username=" ",stream=" ",year=" "):
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student2 WHERE SAPID=? OR username=? OR stream=? OR year=?",(SAPID,username,stream,year))
    row=cur.fetchall()
    con.close()
    return row

def dataUpdate(id,SAPID=" ",username=" ",stream=" ",year=" "):
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("UPDATE student2 set SAPID=?,username=?,stream=?,year=?, WHERE id=?",(SAPID,username,stream,year,id))
    con.commit()
    con.close()

def findRecc(password=" "):
    con=sqlite3.connect("student2.db")
    cur=con.cursor()
    cur.execute("SELECT password FROM countitem WHERE countt=(SELECT max(countt) FROM countitem)")
    item=""
    for i in cur.fetchone():
        item=i
    return(item)
    con.commit()

    #count=[]
    #for i in range(len(options1)):
    #    count.append(0)
    #for i in range(len(options1)):
     #   count[i]=cur.execute(" select count(*) FROM student2 WHERE passowrd=?",(options1[i]))
    #cur.commit
    #maxindex=count.index(max(count))
    #return options1[maxindex]

studentData()






     
