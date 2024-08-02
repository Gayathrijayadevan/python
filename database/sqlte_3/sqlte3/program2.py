import sqlite3

con=sqlite3.connect("database/sqlte3/sample.db")
try:
    con.execute("create table dtls( name text ,place text,c_no int, address text)") 
except:
    pass

# a=int(input("Enter no. of employees: "))
# for i in range(a):
#             name=str(input("Enter name:"))
#             place=str(input("Enter place:"))
#             c_no=int(input("Enter contact no.:"))
#             address=str(input("Enter address:"))

#             con.execute("insert into dtls(name,place,c_no,address) values(?,?,?,?)",(name,place,c_no,address))
#             con.commit()

# data=con.execute("select student.name,student.age,student.mark,dtls.place,dtls.c_no,dtls.address from student inner join dtls on student.name=dtls.name")
# print("{:<10}{:<6}{:<6}{:<10}{:<15}{:<10}".format("name", "age", "mark","place","contact_no","address"))
# print('_' * 60)
# for i in data:
#     print("{:<10}{:<6}{:<6}{:<10}{:<15}{:<10}".format(i[0], i[1], i[2],i[3],i[4],i[5]))

# data=con.execute("select student.name,student.age,student.mark,dtls.place,dtls.c_no,dtls.address from student left join dtls on student.name=dtls.name")
# for i in data:
#     print(i)
    
# data=con.execute("select student.name,student.age,student.mark,dtls.place,dtls.c_no,dtls.address from dtls left join student on student.name=dtls.name")    
# for i in data:
#     print(i)
    
data=con.execute("select student.name,student.age,student.mark,dtls.place,dtls.c_no,dtls.address from student cross join dtls ")    
for i in data:
    print(i)
        