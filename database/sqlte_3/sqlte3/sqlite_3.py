import sqlite3

con =sqlite3.connect('sample.db') #to create database

try:
    con.execute("create table student(age int, name text , mark real)") # to create table
except:
    pass
con.execute("insert into student(age,name,mark) values(21,'manu',60)")    # to add value to the table
con.commit()


# con =sqlite3.connect('database/sqlte3/demo.db') #to create database

# try:
#     con.execute("create table student(age int, name text , mark real)") # to create table
# except:
#     pass

# a= int(input("enter the number of students:"))
# for i in range(a):
#     name=str(input("Enter name:"))
#     age=int(input("Enter age:"))
#     mark=float(input("Enter mark:"))

#     con.execute("insert into student(age,name,mark) values(?,?,?)",(age,name,mark))
#     con.commit()

# data=con.execute("select * from student")  
# print("{:<10}{:<6}{:<6}".format("age", "name", "mark"))
# print('_' * 68)
# for i in data:
#     print("{:<10}{:<6}{:<6}".format(i[0], i[1], i[2]))
    
# 23/07/2024
# a=input("Enter a name:")
# data=con.execute("select * from student where name=?",(a,))
# print("{:<10}{:<6}{:<6}".format("age", "name", "mark"))
# print('_' * 68)
# for i in data:
#     print("{:<10}{:<6}{:<6}".format(i[0], i[1], i[2]))


# data=con.execute("select * from student where mark>=60")
# print("{:<10}{:<6}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<10}{:<6}{:<6}".format(i[0], i[1], i[2]))


# UPDATE COMMAND
# con.execute("update student set name='haridev' where name='hari'") 
# con .commit()
# data=con.execute("select *from student where name='haridev'")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<6}{:<10}{:<6}".format(i[0], i[1], i[2]))


# DELETE COMMAND

# con.execute("delete from student where name='manoj'") 
# con .commit()
# data=con.execute("select *from student ")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<6}{:<10}{:<6}".format(i[0], i[1], i[2]))

# name=input("Enter the name you want to delete:")
# con.execute("delete from student where name=?",(name,)) 
# con .commit()
# data=con.execute("select *from student ")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<6}{:<10}{:<6}".format(i[0], i[1], i[2]))


# 25/07/2024

# data=con.execute("select *from student where name like '_i%' ")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<6}{:<10}{:<6}".format(i[0], i[1], i[2]))


# data=con.execute("select *from student order by mark desc")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print("{:<6}{:<10}{:<6}".format(i[0], i[1], i[2]))


# data=con.execute("select name from student group by name ")
# print("{:<6}{:<10}{:<6}".format("age", "name", "mark"))
# print('_' *20)
# for i in data:
#     print(i)

# data=con.execute("select name, sum(mark) from student group by name ")    
# for i in data:
#     print(i)








