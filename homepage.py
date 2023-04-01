from tkinter import *

window = Tk()

def predictor():
    window.destroy()
    import predictor


def estimator():
    window.destroy()
    import estimator

window.geometry('925x500+300+200')
window.resizable(False,False)
window.title("REAL ESTATE PRICE PREDiCTOR")
f1=Frame(window,bg='white')
f1.pack(fill=X)
l1=Label(f1,text="Welcome to property price predictor",font=("Microsoft YaHei UI Light",30,'bold'), fg="blue", bg='white')
l1.pack(fill=X,pady=25)
f=Frame(window,bg='white')
f.pack(fill=X)
b1=Button(f,text="Predict",font="arial 25 bold", padx=30,pady=30,command=predictor)
b2=Button(f,text="Estimate",font="arial 25 bold",padx=30,pady=30,command=estimator)
b1.grid(row=3,column=2,padx=150,pady=100)
b2.grid(row=3,column=5,padx=40,pady=100)

window.mainloop()