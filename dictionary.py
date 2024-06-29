# std={'name':'akhil','age':21,'place':'ktm'}
# print(std['name'])
# std['name']='hari'
# print(std['name'])
# std['mark']=50
# print(std['mark'])
# for i in std:
    # print(i,std[i])

std={'name':'akhil','age':21,'place':'ktm'}
# print(std.get("name"))

# print(std.items())

# print(std.keys())

# print(std.values())

# for i,j in std.items():
#     print(i,j)

# std.pop('age')
# print(std.items())

# std.popitem()
# print(std.items())

# std.setdefault("place1")
# print(std.items())

# std.update({'place':'ekm'})
# print(std.items())

# std.update({'mark':'20'})
# print(std.items())


dtl=[]
a=int(input("enter no. of students"))
for i in a:
    name=input("enter name:")
    age=int(input("enter age:"))
    course=input("enter course:")
    place=input("enter course:")
    dtl.append({'name':name,'age:'age,'course:'course,'place:'place})    
print("{:<10}{:<6}".format("name","age","course","place"))
print('_'*20)
for i in dtl:
    print(("{:<10}{:<6}").formate(i['name'],i['age'],i['course'],i['place']))

      



