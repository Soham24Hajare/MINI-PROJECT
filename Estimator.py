from logging import root
import tkinter as tk

from matplotlib import image

class RealEstatePredictorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        font=() 
        self.title("Future Price Estimator")
        self.geometry('925x500+300+200')
        
        
        
        # Create a label widget to hold the background image
        self.background_image = tk.PhotoImage(file="Background1.png")
        self.background_label =tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label = tk.Label(self, text=" Estimate The Future Price Here ")
        self.label.config(font=("Arial", 20))
        self.label.pack(pady=60)
        self.Present_value = tk.Label(self, text="Enter Present Value:")
        self.Present_value.config(font=("Arial", 15))
        self.Present_value.pack(pady=5)
        self.Present_value_Entry = tk.Entry(self)
        self.Present_value_Entry.config(font=("Arial", 15))
        self.Present_value_Entry.pack(pady=5)

        self.Growth_rate = tk.Label(self, text="Enter Growth Rate:")
        self.Growth_rate.config(font=("Arial", 15))
        self.Growth_rate.pack(pady=5)
        self.Growth_rate_Entry = tk.Entry(self)
        self.Growth_rate_Entry.config(font=("Arial", 15))
        self.Growth_rate_Entry.pack(pady=5)

        self.Time_period = tk.Label(self, text="Enter Time Period:")
        self.Time_period.config(font=("Arial", 15))
        self.Time_period.pack(pady=5)
        self.Time_period_Entry = tk.Entry(self)
        self.Time_period_Entry.config(font=("Arial", 15))
        self.Time_period_Entry.pack(pady=5)

        self.predict_button = tk.Button(self, text="Predict", command=self.predict)
        self.predict_button.config(font=("Arial", 15))
        self.predict_button.pack(pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=60)
        
    
       
        
        
        
        
    def predict(self):
        # Get the input values
        presentValue = int(self.Present_value_Entry.get())
        growthRate = int(self.Growth_rate_Entry.get())
        timePeriod = float(self.Time_period_Entry.get())

        # Make the prediction
        price = predict_price(presentValue, growthRate, timePeriod)

        # Update the result label
        self.result_label.config(text=f"Estimated Price: {price:.2f}")
        self.result_label.config(font=("Arial", 15))

def predict_price(Present_value,Growth_rate,Time_period):
    # Replace this with your actual prediction code
    # This is just a placeholder
    return Present_value*(1+Growth_rate)**Time_period
    #return bedrooms * 10000 + bathrooms * 5000 + size * 100
    
    

if __name__ == "__main__":
    app = RealEstatePredictorGUI()
    app.mainloop()

