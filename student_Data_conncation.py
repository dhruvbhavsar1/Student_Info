import sqlite3
DB="student.db"
#Creat Tabel
def Tabel_crt():
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute('''
             CREATE TABLE IF NOT EXISTS  STUDENT(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                age TEXT NOT NULL,
                Course TEXT NOT NULL,
                Email TEXT UNIQUE NOT NULL
          )
     ''')
    conn.commit()
    conn.close()
#insert
def Add_Student (name,age,course,Email):
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute("INSERT INTO STUDENT (name,age,Course,Email) VALUES(?,?,?,?)",(name,age,course,Email))
    conn.commit()
    conn.close()

#Update
def Update_Student(s_id,name,age,Course,Email):
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute("UPDATE STUDENT SET name=?,age=?,Course=?,Email=? WHERE ID=?",(s_id,name,age,Course,Email))
    conn.commit()
    conn.close()
#Delete
def Delete_Student(s_id):
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute("DELETE FROM STUDENT WHERE ID=?",(s_id))
    conn.commit()
    conn.close()
#search student
def Search_Student(keyword):
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute('''
           SELECT * FROM STUDENT WHERE name LIKE ? OR Course LIKE ? OR Email LIKE ?
    ''',(f"%{keyword}%",f"%{keyword}%",f"%{keyword}%"))
    result=cmd.fetchall()
    conn.commit()
    conn.close()
    return result
#Display 
def Display():
    conn=sqlite3.connect(DB)
    cmd=conn.cursor()
    cmd.execute("SELECT * FROM STUDENT  ORDER BY ID ASC")
    reow=cmd.fetchall()
    conn.commit()
    conn.close()
    return reow
#print("all done")