# 8/07/2024

# f=open('python/file_handle/new.txt','x')
# f.write('welcome all')

# f=open('python/file_handle/new3.txt','x')
# f.write("123"+"567")

# f=open('python/file_handle/new4.txt','w')
# f.write('hai')

# a=int(input("enter the number of students"))
# f=open('python/file_handle/new4.txt','w')
# for i in range(a):
#     n=input(("Enter name:"))
#     f.write(n)

# a=int(input("enter a number:"))
# f=open('python/file_handle/new5.txt','w')
# for i in range(1,11):
#     n=i*a
#     f.write(f"{i}*{a}={n}\n")

# f = open("python/file_handle/new6.txt", "w")
# a = int(input("Enter the number :"))
# for i in range(1,a+1):
#     for j in range(1, 11):
#         b = str(j) + " * " + str(a) + " = " + str(j * a) + "\n"
#         f.write(b)
#     a-=1
#     f.write('\n')

# 11/07/2024

# f=open("python/file_handle/new.txt","a")
# f.write("to python")

# f=open("python/file_handle/new.txt","r")
# print(f.read())

# f=open("python/file_handle/new.txt","r")
# print(f.read(5))
# print('_'*20)
# print(f.read(5))

# f=open("python/file_handle/new.txt","r")
# print(f.readline(5))
# print('_'*20)
# print(f.readline(3))
# print(f.readline())

# f=open("python/file_handle/new.txt","r")
# print(f.readlines())
# print('_'*20)

# f=open("python/file_handle/new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# for i in range(l):
#     a=f.readline().strip()
#     print(a[::-1])

# f=open("python/file_handle/new.txt","r")
# l=len(f.readlines())
# f.seek(0)
# word=0
# for i in range(l):
#     a=f.readline().strip()
#     for j in a:
#         if j==' ':
#             word+=1
#     word+=1
# print(word)    

f=open("python/file_handle/new.txt","r")
l=len(f.readlines())
f.seek(0)
word=0
let=0
cap=0
for i in range(l):
    a=f.readline().strip()
    for j in a:
        if j==' ':
            word+=1
        else:
            let+=1
            if j.isupper():
                cap+=1   
            
    word+=1
print('words=',word) 
print('letters=',let)
print('capital letters=',cap)
print('small letters=',let-cap)
   











