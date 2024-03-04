import customtkinter as ctk
# from tkinter import simpledialog

# def get_numbers():
#     num1 = simpledialog.askfloat("Enter Number 1", "Enter the first number:")
#     num2 = simpledialog.askfloat("Enter Number 2", "Enter the second number:")
#     num3 = simpledialog.askfloat("Enter Number 3", "Enter the third number:")
#     if num1 is not None and num2 is not None and num3 is not None:
#         print("Numbers entered:", num1, num2, num3)
#     else:
#         print("User canceled")

# # Create main window
# root = tk.Tk()
# root.title("Number Input")

# # Create button to get numbers
# button = tk.Button(root, text="Enter Numbers", command=get_numbers)
# button.pack(pady=10)

# # Run the application
# root.mainloop()

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('drak-blue')

root = ctk.CTk()
root.geometry('600x400')

def parameters():
    print('Please enter the values')

frame=ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Kalman estimation')
label.pack(pady=12, padx=10)

number_of_samples = ctk.CTkEntry(master=frame, placeholder_text='Number of Samples') 
number_of_samples.pack(pady=12,padx=10)

button = ctk.CTkButton(master=frame, text='Run Kalman Filter')
number_of_samples.pack(pady=12,padx=10)

root.mainloop()