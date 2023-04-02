from tkinter import *
import sqlite3
from tkinter import messagebox
import re

from PIL import ImageTk, Image

#GUI
   
win = Tk()
win.geometry("1000x700")
win.title("Home Page")                        
win["bg"] = "#e8f8fa"  


win.resizable(False,False)

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(x=20,y=150)

image = Image.open("homepage.png")

# Resize the image using resize() method
resize_image = image.resize((600,400))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(frame,image=img)
label1.image = img
label1.pack()
label1.place(x=0,y=0)

#Form Title
label_title = Label(win,text ="Welcome to Property Price Predictor",fg="white",width = 30,bg="#485c63",font = ("bold",25)).place(x=220,y=40)

def predictor():
    win.destroy()
    import predictor


def estimator():
    win.destroy()
    import estimator
    
def about():
    win.destroy()
    import moreInfo

#Create fields
b1=Button(win,text="Predict",font="arial 18 bold",fg="white", padx=38,pady=30,command=predictor,bg="#485c63").place(x=700,y=150)

#b1.pack(side="top")
b2=Button(win,text="Estimate",font="arial 18 bold",fg="white",padx=29,pady=30,command=estimator,bg="#485c63").place(x=700,y=300)
#b2.pack(side="top")
b1=Button(win,text="MoreInfo",font="arial 18 bold",fg="white", padx=27,pady=30,command=about,bg="#485c63").place(x=700,y=450)

win.mainloop()
