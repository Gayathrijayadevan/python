def remove(dtl):
    id=int(input("enter student id to be deleted:"))
    for i in dtl:
        if i["id"]==id:
            dtl.remove(i)
            print("The profile has been  deleted")
            break
        else:
            print("invalid id")        
