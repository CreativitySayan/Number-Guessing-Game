import random
import tkinter as tk
from tkinter import messagebox

# Define global variables
lower_bound = 1
upper_bound = 1000
secret_number = None
attempts = 0
max_attempts = 10

# Initialize the game with default difficulty
def initialize_game():
    global secret_number, attempts, max_attempts, lower_bound, upper_bound
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

# Set difficulty based on user choice
def set_difficulty(level):
    global lower_bound, upper_bound, max_attempts
    if level == "Easy":
        lower_bound, upper_bound = 1, 100
        max_attempts = 10
    elif level == "Medium":
        lower_bound, upper_bound = 1, 500
        max_attempts = 8
    else:  # Hard
        lower_bound, upper_bound = 1, 1000
        max_attempts = 5
    initialize_game()
    update_status(f"Guess a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts.")

# Update the status label
def update_status(message):
    status_label.config(text=message)

# Check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        if lower_bound <= guess <= upper_bound:
            attempts += 1
            if guess == secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the secret number {secret_number} in {attempts} attempts!")
                ask_replay()
            elif guess < secret_number:
                update_status(f"Too low! Attempts left: {max_attempts - attempts}")
            else:
                update_status(f"Too high! Attempts left: {max_attempts - attempts}")
            
            if attempts >= max_attempts:
                messagebox.showwarning("Game Over", f"Sorry, you ran out of attempts! The secret number was {secret_number}.")
                ask_replay()
        else:
            update_status(f"Please enter a number between {lower_bound} and {upper_bound}.")
    except ValueError:
        update_status("Invalid input. Please enter a valid number.")

# Ask the player if they want to play again
def ask_replay():
    if messagebox.askyesno("Play Again?", "Would you like to play again?"):
        guess_entry.delete(0, tk.END)
        set_difficulty(difficulty_var.get())
    else:
        root.quit()

# Initialize GUI window
root = tk.Tk()
root.title("Number Guessing Game")

# Difficulty selection
difficulty_var = tk.StringVar(value="Medium")
tk.Label(root, text="Select Difficulty:").pack(pady=10)
tk.Radiobutton(root, text="Easy (1-100)", variable=difficulty_var, value="Easy", command=lambda: set_difficulty("Easy")).pack()
tk.Radiobutton(root, text="Medium (1-500)", variable=difficulty_var, value="Medium", command=lambda: set_difficulty("Medium")).pack()
tk.Radiobutton(root, text="Hard (1-1000)", variable=difficulty_var, value="Hard", command=lambda: set_difficulty("Hard")).pack()

# Entry for guesses
tk.Label(root, text="Enter your guess:").pack(pady=10)
guess_entry = tk.Entry(root)
guess_entry.pack()

# Submit guess button
submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack(pady=10)

# Status label to display messages
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Initialize the game with default settings
set_difficulty(difficulty_var.get())

# Start the GUI event loop
root.mainloop()

