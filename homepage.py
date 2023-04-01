from tkinter import *
root = Tk()

def predictor():
    root.destroy()
    import predictor


def Estimator():
    root.destroy()
    import Estimator

root.geometry('925x500+300+200')
#root.resizable(False,False)
root.title("REAL ESTATE PRICE PREDiCTOR")
f1=Frame(root,bg='white')
f1.pack(fill=X)
l1=Label(f1,text="Welcome to property price predictor",font=("Microsoft YaHei UI Light",30,'bold'), fg="blue", bg='white')
l1.pack(fill=X,pady=25)
f=Frame(root,bg='white')
f.pack(fill=X)
b1=Button(f,text="Predict",font="arial 25 bold", padx=30,pady=30,command=predictor)
b2=Button(f,text="Estimate",font="arial 25 bold",padx=30,pady=30,command=Estimator)
b1.grid(row=3,column=2,padx=150,pady=100)
b2.grid(row=3,column=5,padx=40,pady=100)

root.mainloop()