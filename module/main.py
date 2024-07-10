# 6/07/2024

from reg import *
from display import *
from update import *
from delete import *
dtl=[]
while True:
    print("1.Add \n 2.Display \n 3.Update \n 4.Delete \n. 5.exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        register(dtl)
    elif ch==2:
        view(dtl)
    elif ch==3:
        change(dtl)  
    elif ch==4:
        remove(dtl)
    elif ch==5:
        break
