def remove(dtl):
    a_id=input("enter student id:")
    f=0
    for i in dtl:
        if a_id in dtl:
            a_key=input("enter the you want to delete:")
            i.pop(a_key)
