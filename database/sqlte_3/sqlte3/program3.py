import sqlite3

con=sqlite3.connect("database/sqlte3/new.db")
try:
    con.execute("create table employee( name text ,designation text,experience int, salary int)") 
except:
    pass

a=int(input("Enter no. of employees: "))
for i in range(a):
            name=str(input("Enter name:"))
            designation=str(input("Enter designation:"))
            experience=int(input("Enter experience.:"))
            salary=str(input("Enter salary:"))

            con.execute("insert into employee(name,designation,experience,salary) values(?,?,?,?)",(name,designation,experience,salary))
            con.commit()
