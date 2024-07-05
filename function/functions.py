# def fun1():
#     print('welcome')

# fun1()    



# print('hai')
# def fun1():
    # print('welcome')
# 
# 
# print("all")
# fun1()    


# def add():


# 3/06/2024

# a=20 #global variable
# def fun():
    # a=10 #local variable
    # print("in",a)
# 
# fun()    
# print("out",a)

# a=20 #global variable
# def fun():
    # a=20 #local variable
    # a+=10
    # print("in",a)
# 
# fun()    
# print("out",a)

# a=20 #global variable
# def fun():
#      global b
#      b=10  #local variable
#      print("in",b)
# fun()     
# print("out",b)

# a=20 #global variable
# def fun():
    #  global b
    #  b=10  #local variable
    #  print("in",b)
    #  c=45
    #  return c,75
# c1,d1=fun()     
# print("out",c1,d1)

# def add(a,b):
    # return(a+b)
# 
# print(add(10,20))
# print(add(10,30))
# print(add(10,40))
# print(add('ha','ri'))

# def add(name,age=22):
#     return(name,age)

# print(add('nia',21))
# print(add('manu'))

# def add(name,age):
    # print("name:",name)
    # print("age:",age)
# 
# add('nia',21)
# add(21,'priya')
# add(name='priya',age=21)
# print('out')

# def add(*a):
#     return a

# print(add('priya',21))


# def add(**a):
    # return a
# 
# print(add(name='priya',age=21))
# print(add())


# 4/06/2024


# def add(a,b):
    # return a+b
# 
# def sub(a,b):
    # return a-b
# 
# def mul(a,b):
    # return a*b
# 
# def div(a,b):
    # return a/b
# 
# def numbers():
    # a=int(input("enter a number"))
    # b=int(input("enter another number"))
    # return a,b
# 
# while True:
    # print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division\n 5. exit")
    # ch=int(input("enter your choice:"))
# 
    # if ch==1:
        # a,b=numbers()
        # print("Result:",add(a,b))
    # elif ch==2:
        # a,b=numbers()
        # print("Result:",sub(a,b))
    # elif ch==3:
        # a,b=numbers()    
        # print("Result:",mul(a,b))
    # elif ch==4:
        # a,b=numbers()    
        # print("Result:",div(a,b))
    # elif ch==5:
        # break

# LAMPDA FUNCTION

# add=lambda a,b:a+b
# print(add(10,15))

# 1.
# def add(a,b):
    # return a+b
# 
# def sub(a,b):
    # return a-b
# 
# mul=lambda a,b:a*b
# 
# div=lambda a,b:a/b
# 
# def numbers():
    # a=int(input("enter a number:"))
    # b=int(input("enter another number:"))
    # return a,b
# 
# while True:
    # print("1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division\n 5. exit")
    # ch=int(input("enter your choice:"))
# 
    # if ch==1:
        # a,b=numbers()
        # print("Result:",add(a,b))
    # elif ch==2:
        # a,b=numbers()
        # print("Result:",sub(a,b))
    # elif ch==3:
        # a,b=numbers()    
        # print("Result:",mul(a,b))
    # elif ch==4:
        # a,b=numbers()    
        # print("Result:",div(a,b))
    # elif ch==5:
        # break

# MAP        

# 1.

# l=[1,2,3,4,5]
# data=map(lambda a:a**2,l)
# print(list(data))

# def data(a):
    # return a**2
# 
# data1=map(data,l)
# print(list(data1))

# l=[1,2,3,4,5]

# data=filter(lambda a:a%2==0,l)
# print(list(data))

# def data(a):
    # return a%2==0
# data=filter(data,l)
# print(list(data))

# l=['apple','mango']
# 
# def fun(a):
    # return a[0]=='a'
# data=filter(fun,l)
# print(list(data))

# import functools
# i=[1,2,3,4,5]
# data=functools.reduce(lambda total,values:total*values,i)
# print(data)






