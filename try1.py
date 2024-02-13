import tkinter
from tkinter import *
m=tkinter.Tk()
m.title("Student login form")
m.maxsize(width='600', height='600')
m.minsize(width="500", height="400")

heading=Label(m,text="Log in", font="Arial")
heading.place(x=100, y=20)

username=StringVar()
usertext=Entry(m,width=50)
usertext.place(x=20,y=20)


usertext.pack()

m.mainloop()
