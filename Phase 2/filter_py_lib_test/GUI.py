'''
https://www.youtube.com/watch?v=Miydkti_QVE 

https://www.youtube.com/playlist?list=PLfZw_tZWahjxJl81b1S-vYQwHs_9ZT77f 

https://www.youtube.com/watch?v=0H19QzbBqC4 

'''

import tkinter
import customtkinter as ctk
import kf_algorithm

def RunProgram():
    try:
        val_1 = int(sample_size.get())
        kf_algorithm.main(val_1)
    except ValueError:
        tkinter.messagebox.showerror('Error','Please Enter a valid number')



# Apperance settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# App frame
app = ctk.CTk()
app.geometry('720x480')
app.title('Kalman Filter Algorithm')

font_1 = ctk.CTkFont(family='Calibri',size=14, weight='bold')

#Adding UI elements
# Sample Size
label_1=ctk.CTkLabel(app, text="Sample Size",font=font_1)
label_1.pack(padx=10,pady=10)
label_1.place(relx=0.1,rely=0.1,anchor=tkinter.CENTER)

sample_size = ctk.CTkEntry(app,width=200, height=30)
sample_size.pack(padx=10,pady=10)
sample_size.place(relx=0.3,rely=0.1,anchor=tkinter.CENTER)

# Noise Mean
# label_2 = ctk.CTkLabel(app,text='Mean value of Noise')


# Noise Standard Deviation



# Plot Button
plot = ctk.CTkButton(app, text="Plot Graph", corner_radius=32, command=RunProgram,
                     fg_color='#0096C7',hover_color='#00B4D8',border_color='#023E8A',
                     border_width=1.5, font=font_1)
plot.pack(padx=10,pady=10)
plot.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)

# Run app
app.mainloop()
