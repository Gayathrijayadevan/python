# 8/07/2024

# f=open('python/file_handle/new.txt','x')
# f.write('welcome all')

# f=open('python/file_handle/new3.txt','x')
# f.write("123"+"567")

# f=open('python/file_handle/new4.txt','w')
# f.write('hai')

a=int(input("enter the number of students"))
f=open('python/file_handle/new4.txt','w')
for i in range(a):
    n=input(("Enter name:"))
    f.write(n)


