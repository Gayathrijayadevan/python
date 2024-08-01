import tkinter
from tkinter import messagebox

app=tkinter.Tk()  #to create an app

def data():
    # print(v1.get())
    # v=v1.get()
    # l2.config(text=v)
    # messagebox.showinfo("display",v1.get())
    # messagebox.askquestion("display",v1.get())
    # messagebox.askretrycancel("display",v1.get())
    # messagebox.askyesnocancel("display",v1.get())
    # messagebox.askokcancel("display",v1.get())
    if v_c1.get()==1:
        print("malayalam selected")
    if v_c2.get()==1:
        print("english selected")
    print(vr1.get())    

app.title("synnfeo")  #to add app title
app.minsize(400,400)  #to specify min & max size
app.maxsize(600,600)
app.config(bg="grey")  #to specify the bg colour

l1=tkinter.Label(app,text="welcome",bg="red",fg="white")   #to add some text/label to the app
l1.pack()

v1=tkinter.StringVar()
e1=tkinter.Entry(app,textvariable=v1)  #to add an entry box
e1.pack()

v_c1=tkinter.IntVar()
v_c2=tkinter.IntVar()
c1=tkinter.Checkbutton(app,text="mal",variable=v_c1)  #to add checkbox
c1.pack()
c2=tkinter.Checkbutton(app,text="eng",variable=v_c2)
c2.pack()

r1=tkinter.Radiobutton(app,text="male",variable=vr1)
r2=tkinter.Radiobutton(app,text="female",variable=vr1)
vr1=tkinter.IntVar()

b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="blue",activeforeground="white",padx=10,pady=10,command=data)  #to add a button 
# a function is also added to this to save the value entered in entry box whwn thw button is clicked
b1.pack() 

# l2=tkinter.Label(app)
# l2.pack()

app.mainloop()