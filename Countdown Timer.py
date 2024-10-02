import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown
def start_countdown():
    try:
        total_seconds = int(hours_var.get()) * 3600 + int(minutes_var.get()) * 60 + int(seconds_var.get())
    except ValueError:
        messagebox.showwarning("Warning", "Please enter valid numbers for hours, minutes, and seconds.")
        return
    
    if total_seconds <= 0:
        messagebox.showwarning("Warning", "The countdown time must be greater than 0.")
        return

    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)
        time_format = f"{hours:02}:{mins:02}:{secs:02}"
        time_var.set(time_format)
        root.update()
        time.sleep(1)
        total_seconds -= 1

    messagebox.showinfo("Time's up!", "The countdown has finished!")

# Function to reset the timer
def reset_timer():
    hours_var.set("00")
    minutes_var.set("00")
    seconds_var.set("00")
    time_var.set("00:00:00")

# Initialize the GUI window
root = tk.Tk()
root.title("Countdown Timer")

# Variables to hold the time
hours_var = tk.StringVar(value="00")
minutes_var = tk.StringVar(value="00")
seconds_var = tk.StringVar(value="00")
time_var = tk.StringVar(value="00:00:00")

# Input fields for hours, minutes, and seconds
tk.Label(root, text="Hours:").pack(pady=5)
tk.Entry(root, textvariable=hours_var, width=3, font=("Courier", 24)).pack(pady=5)

tk.Label(root, text="Minutes:").pack(pady=5)
tk.Entry(root, textvariable=minutes_var, width=3, font=("Courier", 24)).pack(pady=5)

tk.Label(root, text="Seconds:").pack(pady=5)
tk.Entry(root, textvariable=seconds_var, width=3, font=("Courier", 24)).pack(pady=5)

# Display countdown
tk.Label(root, textvariable=time_var, font=("Courier", 36), fg="red").pack(pady=20)

# Start and reset buttons
start_button = tk.Button(root, text="Start Timer", command=start_countdown)
start_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Timer", command=reset_timer)
reset_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
