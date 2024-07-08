def change(dtl):
    id=int(input("enter student id:"))
    f=0
    for i in dtl:
        if  i["id"]==id:
            n_name=input("Enter the new name")
            i.update({'name':n_name})

            n_age=int(input("enter the new age:"))
            i.update({'age':n_age})

            n_place=input("enter the new place:")
            i.update({'place':n_place})
            f=1

    if f==0:   
            print("sorry invalid key,try again")        