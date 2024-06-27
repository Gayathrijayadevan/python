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
l=[1,2,3,'abc',20.5]
n=0
m=0
s=0
for i in l:
 if type(i)==int:
      n+=i
 elif type(i)==float:
      n+=i 
print(n)


          

