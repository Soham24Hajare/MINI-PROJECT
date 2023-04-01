from tkinter import *


root=Tk()
root.title('Future Price Estimator')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)


def predict():
    # Get the input values
    presentValue = int(Present_value_Entry.get())
    growthRate = int(Growth_rate_Entry.get())
    timePeriod = float(Time_period_Entry.get())

    # Make the prediction
    price = predict_price(presentValue, growthRate, timePeriod)

    # Update the result label
    result_label.config(text=f"Estimated Price: {price:.2f}")
    result_label.config(font=("Arial", 15))


def predict_price(Present_value,Growth_rate,Time_period):
    # Replace this with your actual prediction code
    # This is just a placeholder
    return Present_value*(1+Growth_rate/100)**Time_period
    #return bedrooms * 10000 + bathrooms * 5000 + size * 100

def home():

    import homepage

background_image = PhotoImage(file="background1.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
label=Label(root, text=" Estimate The Future Price Here ")
label.config(font=("Arial", 20))
label.pack(pady=60)

Present_value = Label(root, text="Enter Present Value:")
Present_value.config(font=("Arial", 15))
Present_value.pack(pady=5)
Present_value_Entry = Entry()
Present_value_Entry.config(font=("Arial", 15))
Present_value_Entry.pack(pady=5)

Growth_rate = Label(root, text="Enter Growth Rate:")
Growth_rate.config(font=("Arial", 15))
Growth_rate.pack(pady=5)
Growth_rate_Entry = Entry()
Growth_rate_Entry.config(font=("Arial", 15))
Growth_rate_Entry.pack(pady=5)

Time_period = Label(root, text="Enter Time Period:")
Time_period.config(font=("Arial", 15))
Time_period.pack(pady=5)
Time_period_Entry = Entry()
Time_period_Entry.config(font=("Arial", 15))
Time_period_Entry.pack(pady=5)

predict_button = Button(root, text="Predict", command=predict)
predict_button.config(font=("Arial", 15))
predict_button.pack(pady=5)

result_label = Label(root, text="")
result_label.pack(pady=5)

homep= Button(root,width=6,text='Back',border=0,
                bg='white',font=("Arial", 15)
                ,command=home)
homep.place(x=10,y=10)




root.mainloop()
