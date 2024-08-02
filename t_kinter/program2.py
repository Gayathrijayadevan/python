import tkinter

app=tkinter.Tk()
c=tkinter.Canvas(app,height=400,width=400,bg="red")  #to create a canvas

c.create_line(0,150,400,150)  #to create a line.the values specify the starting & ending points

c.create_rectangle(50,50,350,350,fill="blue")   #to create a rectangle,the values specify the starting , ending points & its length & breadth

c.create_oval(50,50,350,350,fill="yellow")  #to create a circle/oval

c.pack()
c.mainloop()