from tkinter import *
p= Tk()

def enter():
    #a=area.get()
    #print(a)
    #p.destroy()
   # import output
    import mlcode
    from joblib import dump, load
    import numpy as np
    model = load('Dragon.joblib')
    b = np.array([[0, area.get(), 0, 0, 0, room.get(), age.get(), 0, 0, tax.get(), 0, 0, 0]])
   # print(b)
    a = model.predict(b)
    d=Entry(f2,font="20")
    d.insert(0,a)
    d.grid(row=8,column=1,pady=40)
    Label(f2,text="Predicted prize(in 1000$)",font="arial 20 bold").grid(row=8,column=0, padx=15)

f1 = Frame(p,width=550,height=40, bg="black")
f1.pack(fill=X)
f2=Frame(p,width=550,height=400)
f2.pack(fill=X, pady=30)
p.geometry("925x550")
#p.maxsize(650, 550)
l1 = Label(f1,text="Welcome to Predictor",font=("Microsoft YaHei UI Light",30,'bold'), fg="blue", bg='white',padx=30)
l2 = Label(f2,text="Area in sqft.",font="arial 20 bold")
l3 = Label(f2,text="No. of rooms",font="arial 20 bold")
l4 = Label(f2,text="Age of the property",font="arial 20 bold")
l5 = Label(f2,text="Total Tax",font="arial 20 bold")

#l1.grid(row=1,column=0,padx=90)
l1.pack(fill=X)
l2.grid(row=2,column=0,pady=15)
l3.grid(row=3,column=0,pady=15)
l4.grid(row=4,column=0,pady=15,padx=15)
l5.grid(row=5,column=0,pady=15)

area=StringVar()
room=StringVar()
age=StringVar()
tax=StringVar()

Entry(f2,textvariable=area, font="arial 17").grid(row=2,column=1,padx=20)
Entry(f2,textvariable=room, font="arial 17").grid(row=3,column=1)
Entry(f2,textvariable=age, font="arial 17").grid(row=4,column=1)
Entry(f2,textvariable=tax, font="arial 17").grid(row=5,column=1)

Button(f2, text="Submit",font="arial 20 bold", command=enter).grid(row=7,column=1)

p.mainloop()