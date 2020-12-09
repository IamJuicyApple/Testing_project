import sqlite3



conn = sqlite3.connect("database.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS name_id(ID INT, name TEXT, IC INT )")

def new_user():
    name = input("Name: ")
    IC = int(input("IC: "))
    c.execute("INSERT INTO name_id(ID,name,IC)VALUES(?,?,?)",
              (ID,name,IC))
    conn.commit()

def read_name_id():
    c.execute("SELECT * FROM name_id WHERE ID = {}".format(ID))
    for row in c.fetchall():
        print(row[1])
 
create_table()

ID = int(input("ID : "))
while ID!=999:
    if 1111111<=ID<=9999999:
        options = input("Are you a New User? (Y/N) : ")
        if options=="Y" or options=="y":
            new_user()
            read_name_id()



        elif options=="N" or options=="n":
            read_name_id()
     
    ID = int(input("ID : "))            

c.close()
conn.close()















##ID = int(input("ID : "))
##while ID!=999:
##    if 1111111<=ID<=9999999:
##        c.execute("SELECT * FROM name_id WHERE ID = {}".format(ID))
##        for row in c.fetchall():
##            if ID != row[0]:
##                print("Hi, new user.. \n Please Enter Your Personal Information")
##                new_user()
##                read_name_id()
##            
##            else:
##                read_name_id()
##            break
##    ID = int(input("ID : "))            

