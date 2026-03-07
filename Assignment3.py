# Program Name: Assignment3.py
# Course: IT3883 / Section 01
# Student Name: Jaleelah Bachou
# Assignment Number: Lab 3
# Due Date: 03/06/2026
# Purpose:
# This program creates a GUI that converts Miles per Gallon (MPG)
# into Kilometers per Liter (KM/L). The result automatically updates
# whenever the user types a value. The program also handles invalid
# inputs such as letters or empty boxes without crashing.
# Resources Used:
# course notes and personal coding practice.
import tkinter as tk
MPG_TO_KML = 0.425143707

# function to perform conversion
def convert(event=None):
    try:
        mpg = float(entry_mpg.get())
        kml = mpg * MPG_TO_KML
        result.set(f"{kml:.3f} km/l")
    except:
        result.set("Enter a valid number")

# create window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("350x200")

# MPG label
label1 = tk.Label(window, text="Miles per Gallon:")
label1.pack(pady=10)

# entry box
entry_mpg = tk.Entry(window)
entry_mpg.pack()

# update result whenever user types
entry_mpg.bind("<KeyRelease>", convert)

# result label
label2 = tk.Label(window, text="Kilometers per Liter:")
label2.pack(pady=10)

result = tk.StringVar()
label_result = tk.Label(window, textvariable=result, font=("Arial", 14))
label_result.pack()

# run program
window.mainloop()
