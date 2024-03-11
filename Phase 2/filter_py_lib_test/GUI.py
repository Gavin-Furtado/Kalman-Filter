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
        n_mean = float(mean_noise.get())
        n_std = float(noise_std.get())
        initial_P = [int(x_pos_err.get()),int(y_pos_err.get()), int(x_vel_err.get()), int(y_vel_err.get())]
        R_matrix =[int(x_pos_obs_err.get()),int(y_pos_obs_err.get()), int(x_vel_obs_err.get()), int(y_vel_obs_err.get())]
        kf_algorithm.main(val_1, n_mean, n_std, initial_P,R_matrix)
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
sample_size.place(relx=0.35,rely=0.1,anchor=tkinter.CENTER)

# Noise Mean
label_2 = ctk.CTkLabel(app,text='Mean value of Noise', font=font_1)
label_2.pack(padx=10,pady=10)
label_2.place(relx=0.1,rely=0.2,anchor=tkinter.CENTER)

mean_noise = ctk.CTkEntry(app,width=200, height=30)
mean_noise.pack(padx=10,pady=10)
mean_noise.place(relx=0.35,rely=0.2,anchor=tkinter.CENTER)

# Noise Standard Deviation
label_3 = ctk.CTkLabel(app,text='Nosie Standard Deviation', font=font_1)
label_3.pack(padx=10,pady=10)
label_3.place(relx=0.1,rely=0.3,anchor=tkinter.CENTER)

noise_std = ctk.CTkEntry(app,width=200, height=30)
noise_std.pack(padx=10,pady=10)
noise_std.place(relx=0.35,rely=0.3,anchor=tkinter.CENTER)

# Process Covariance Matrix
label_4 = ctk.CTkLabel(app,text='Initial Process Covariance Matrix', font=font_1)
label_4.pack(padx=10,pady=10)
label_4.place(relx=0.75,rely=0.1,anchor=tkinter.CENTER)

label_5 = ctk.CTkLabel(app,text='x-position error', font=font_1)
label_5.pack(padx=10,pady=10)
label_5.place(relx=0.7,rely=0.2,anchor=tkinter.CENTER)

x_pos_err = ctk.CTkEntry(app,width=100, height=30)
x_pos_err.pack(padx=10,pady=10)
x_pos_err.place(relx=0.85,rely=0.2,anchor=tkinter.CENTER)

label_6 = ctk.CTkLabel(app,text='y-position error', font=font_1)
label_6.pack(padx=10,pady=10)
label_6.place(relx=0.7,rely=0.3,anchor=tkinter.CENTER)

y_pos_err = ctk.CTkEntry(app,width=100, height=30)
y_pos_err.pack(padx=10,pady=10)
y_pos_err.place(relx=0.85,rely=0.3,anchor=tkinter.CENTER)

label_7 = ctk.CTkLabel(app,text='x-velocity error', font=font_1)
label_7.pack(padx=10,pady=10)
label_7.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)

x_vel_err = ctk.CTkEntry(app,width=100, height=30)
x_vel_err.pack(padx=10,pady=10)
x_vel_err.place(relx=0.85,rely=0.4,anchor=tkinter.CENTER)

label_8 = ctk.CTkLabel(app,text='y-velocity error', font=font_1)
label_8.pack(padx=10,pady=10)
label_8.place(relx=0.7,rely=0.5,anchor=tkinter.CENTER)

y_vel_err = ctk.CTkEntry(app,width=100, height=30)
y_vel_err.pack(padx=10,pady=10)
y_vel_err.place(relx=0.85,rely=0.5,anchor=tkinter.CENTER)

# R_matrix
label_9 = ctk.CTkLabel(app,text='Observation Error Matrix (R_matrix)', font=font_1)
label_9.pack(padx=10,pady=10)
label_9.place(relx=0.15,rely=0.4,anchor=tkinter.CENTER)

label_10 = ctk.CTkLabel(app,text='x-position observation error', font=font_1)
label_10.pack(padx=10,pady=10)
label_10.place(relx=0.15,rely=0.45,anchor=tkinter.CENTER)

x_pos_obs_err = ctk.CTkEntry(app,width=60, height=20)
x_pos_obs_err.pack(padx=10,pady=10)
x_pos_obs_err.place(relx=0.33,rely=0.45,anchor=tkinter.CENTER)

label_11 = ctk.CTkLabel(app,text='y-position observation error', font=font_1)
label_11.pack(padx=10,pady=10)
label_11.place(relx=0.15,rely=0.5,anchor=tkinter.CENTER)

y_pos_obs_err = ctk.CTkEntry(app,width=60, height=20)
y_pos_obs_err.pack(padx=10,pady=10)
y_pos_obs_err.place(relx=0.33,rely=0.5,anchor=tkinter.CENTER)

label_12 = ctk.CTkLabel(app,text='x-velocity observation error', font=font_1)
label_12.pack(padx=10,pady=10)
label_12.place(relx=0.15,rely=0.55,anchor=tkinter.CENTER)

x_vel_obs_err = ctk.CTkEntry(app,width=60, height=20)
x_vel_obs_err.pack(padx=10,pady=10)
x_vel_obs_err.place(relx=0.33,rely=0.55,anchor=tkinter.CENTER)

label_13 = ctk.CTkLabel(app,text='y-velocity observation error', font=font_1)
label_13.pack(padx=10,pady=10)
label_13.place(relx=0.15,rely=0.6,anchor=tkinter.CENTER)

y_vel_obs_err = ctk.CTkEntry(app,width=60, height=20)
y_vel_obs_err.pack(padx=10,pady=10)
y_vel_obs_err.place(relx=0.33,rely=0.6,anchor=tkinter.CENTER)



# Plot Button
plot = ctk.CTkButton(app, text="Plot Graph", corner_radius=32, command=RunProgram,
                     fg_color='#0096C7',hover_color='#00B4D8',border_color='#023E8A',
                     border_width=1.5, font=font_1)
plot.pack(padx=10,pady=10)
plot.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)

# Run app
app.mainloop()
