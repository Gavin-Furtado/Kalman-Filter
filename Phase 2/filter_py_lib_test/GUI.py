import tkinter
import customtkinter as ctk
import kf_algorithm

def RunProgram():
    try:
        val_1 = int(sample_size.get())
        kf_algorithm.main(val_1)
    except ValueError:
        ctk.messagebox.showerror('Error','Please Enter a valid number')



# Apperance settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# App frame
app = ctk.CTk()
app.geometry('720x480')
app.title('Kalman Filter Algorithm')

#Adding UI elements
label_1=ctk.CTkLabel(app, text="Sample Size")
label_1.pack(padx=10,pady=10)

sample_size = ctk.CTkEntry(app,width=200, height=30)
sample_size.pack(padx=10,pady=10)

# Plot Button
plot = ctk.CTkButton(app, text="Plot Graph",command=RunProgram)
plot.pack(padx=10,pady=10)

# Run app
app.mainloop()
