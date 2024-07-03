# 26/6/2024

# name=['manu','akhil','abhi',25,30,35]
# print(name)

# print(name[3])

# if 'manu' in name:
#     print('yes')
# else:
#     print('no')    

# for i in name:
#     print(i)


# names=['akhil','manu','hari']
# a=input("enter the value to e searched:")
# if a in names:
#     print(a,'is in the list')
# else:
#     print(a,'is not in the list')    

# l=[1,2,3,4]

# l.append(5)
# l.append('manu')
# l.append([5,6,7])
# print(l)

# l.insert(4,5)
# print(l)

# l.extend([6,7,8,9])
# print(l)

# l=[1,2,3]
# l.remove(2)
# print(l)

# l.pop()
# print(l)
# l.pop(1)
# print(l)

# l.clear()
# print(l)

# print(l.index(3))
# print(l.index(1))

# l.extend([2,4,2])
# print(l.count(2))

# l.reverse()
# print(l)

# l.sort()
# l.reverse()
# print(l)

# 1.enter names into a list

# a=int(input("Enter no. of students:"))
# names=[]
# for i in range(a):
#      n=input("enter name:")
#      names.append(n)
# print(names)  

# 27/06/2024
# 1.remove duplicate values from the list and print it

# l=[1,2,3,1,2,3]
# n=[]
# for i in l:
#  if i not in n:
#       n.append(i)
# print(n)

# 2.reverse a list

# l=['manu','hari','akhil']
# n=''
# for i in l:
#      for j in i:
#       n=j+n
# print(n)


# 3.add elements of a list
# l=[1,2,3,'abc',20.5]
# n=0
# for i in l:
#  if type(i)==int:
     #  n+=i
#  elif type(i)==float:
     #  n+=i 
# print(n)
# 
#29/06/2024 

# 1.print the largest L=[1,2,10,20,35]
 
# l=[1,2,10,20,35]
# n=l[0]
# for i in l:      
#     if i>n:
     #    n=i
#    
# print(" The largest number is:",n)  

std=[]
while True:
     print("1.Add \n 2.display \n 3.update\n 4.delete \n 5.exit ")
     a=int(input("enter your choice:"))
     if a==1:
          b=int(input ('enter number of students'))
          for i in range(b):
               name=input("Enter the name:")
               age=int(input("Enter age:"))
               class_name=input("Enter class:")
               std.append([name,age,class_name])
     elif a==2:
          for i in std:
               print("student details:")          
               print(i)
     elif a==3:
          f=0
          a_name=input("Enter a name:")    
          for i in std:      
               if a_name in i:
                    age=int (input("Enter nwe age"))
                    i[1]=age
                    f=1
          if f==0:
               print("This student is not in the list")     
     elif a==4:
          aname=input("Enter the name") 
          f=0         
          for i in std:
               if aname in i:
                    std.remove(i)
                    print(aname,"is deleted from the list")
                    f=1
          if f==0:
               print("There is no such name ")          
     elif a==5:
          break               






        



          

