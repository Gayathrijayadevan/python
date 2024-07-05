# def fun1():
    # print("hai")
# 
# def fun2():
    # print("welcome")

def argu1(a,b):
  print("positional:")
  return(a+b)

def argu2(name,age=22):
     print("default:")
     return(name,age)

def argu3(name,age):
     print("keyword:")
     print("name:",name)
     print("age:",age)

def argu4(*a):
    print("arbitary:")
    return a

def argu5(**a):
    print("arbi-key:")
    return a
