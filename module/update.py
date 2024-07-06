def change(dtl):
    f=0
    a=input("enter name of the student:")
    for i in dtl:
        if a in i:
            s_key=input("enter the key you want to update")
            n_value=input("enter the new value")
            i[a]=n_value
            f=1
    if f==0:
        print("sorry invalid key,try again")        