def register(dtl):
        
        id=int(input("Enter id:"))
        name=input("Enter student name:")
        age= int(input("Enter student age:"))
        place=input("Enter place")
        dtl.append({'id':id,'name':name,'age':age,'place':place})