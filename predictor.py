from tkinter import *
import sqlite3
from tkinter import messagebox
import re

from PIL import ImageTk, Image

p= Tk()

#GUI
   
#root = Tk()
#root.geometry("1000x700")
#root.title("Home Page")                        
p["bg"] = "#e8f8fa"  


#p.resizable(False,False)

#frame = Frame(p, width=600, height=400)
#frame.pack()
#frame.place(x=20,y=150)
frame = Frame(p, width=550, height=400)
frame.pack()
frame.place(x=60,y=150)
image = Image.open("1.jpg")

# Resize the image using resize() method
resize_image = image.resize((550,400))
 
img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(frame,image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=0)

def enter():
    a=area.get()
    print(a)
    #p.destroy()
    #import output
    import mlcode
    from joblib import dump, load
    import numpy as np
    model = load('Dragon.joblib')
    b = np.array([[0, area.get(), 0, 0, 0, room.get(), age.get(), 0, 0, tax.get(), 0, 0, 0]])
    #print(b)
    a = model.predict(b)
    d=Entry(font="17")
    d.place(x=950,y=600)
    d.insert(0,a)
    #d.place(x=700,y=150)
    Label(text="Predicted prize(in 1000$)",font="arial 17 bold").place(x=650,y=600)

def home():
    p.destroy()
    import homepage
#f1 = Frame(p,width=550,height=40, bg="black")
#f1.pack(fill=X)
#f2=Frame(p,width=550,height=400)
#f2.pack(fill=X, pady=30)
#p.geometry("925x550")
#p.maxsize(650, 550)
frame1 = Frame(p, width=1500, height=70,bg="#485c63")
frame1.pack()
frame1.place(x=0,y=0)

l1 = Label(frame1,text="Welcome To The Predictor!!",fg="white",bg="#485c63",font=("Microsoft YaHei UI Light",30,'bold'),padx=300).place(x=50,y=10)
l2 = Label(text=" Area in sqft. ",fg="white",bg="#485c63",font="arial 17 bold").place(x=700,y=150)
l3 = Label(text=" No. of rooms ",fg="white",bg="#485c63",font="arial 17 bold").place(x=700,y=220)
l4 = Label(text=" Age ",fg="white",bg="#485c63",font="arial 17 bold").place(x=700,y=290)
l5 = Label(text=" Total Tax ",fg="white",bg="#485c63",font="arial 17 bold").place(x=700,y=360)


area=StringVar()
room=StringVar()
age=StringVar()
tax=StringVar()

Entry(textvariable=area, font="arial 17").place(x=910,y=150)
Entry(textvariable=room, font="arial 17").place(x=910,y=220)
Entry(textvariable=age, font="arial 17").place(x=910,y=290)
Entry(textvariable=tax, font="arial 17").place(x=910,y=360)

Button(text="Submit",font="arial 17 bold",fg="white",bg="#485c63", command=enter).place(x=930,y=430)

#def home():
   # p.destroy()
   # import homepage
    
homep= Button(p,width=6,text='Back',border=0,
                bg='white',font=("Arial", 15)
                ,command=home)
homep.place(x=10,y=17)
p.mainloop()
