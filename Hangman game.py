import random
import tkinter as tk
from tkinter import messagebox

# List of words to choose from
WORDS = ["PYTHON", "DEVELOPER", "COMPUTER", "HANGMAN", "ALGORITHM", "SOFTWARE", "PROGRAMMING", "TECHNOLOGY"]

# Function to choose a random word
def choose_word():
    return random.choice(WORDS)

# Function to update the display word
def update_display_word():
    display_word.set(" ".join([letter if letter in guessed_letters else "_" for letter in word]))

# Function to handle a guessed letter
def guess_letter():
    letter = entry.get().upper()
    entry.delete(0, tk.END)

    if letter in guessed_letters:
        messagebox.showwarning("Warning", "You already guessed that letter.")
    elif len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Warning", "Please enter a single valid letter.")
    else:
        guessed_letters.add(letter)
        if letter in word:
            update_display_word()
            if all([letter in guessed_letters for letter in word]):
                messagebox.showinfo("Congratulations!", f"You've guessed the word: {word}")
                reset_game()
        else:
            update_hangman()
            if wrong_guesses == max_wrong_guesses:
                messagebox.showinfo("Game Over", f"Sorry, you've been hanged! The word was: {word}")
                reset_game()

# Function to update the hangman graphic
def update_hangman():
    global wrong_guesses
    wrong_guesses += 1
    hangman_label.config(text=hangman_stages[wrong_guesses])

# Function to reset the game
def reset_game():
    global word, guessed_letters, wrong_guesses
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    hangman_label.config(text=hangman_stages[0])
    update_display_word()

# Initialize the GUI window
root = tk.Tk()
root.title("Hangman Game")

# Hangman stages
hangman_stages = [
    "_______\n|     |\n|\n|\n|\n|\n|\n-------",
    "_______\n|     |\n|     O\n|\n|\n|\n|\n-------",
    "_______\n|     |\n|     O\n|     |\n|\n|\n|\n-------",
    "_______\n|     |\n|     O\n|    /|\n|\n|\n|\n-------",
    "_______\n|     |\n|     O\n|    /|\\\n|\n|\n|\n-------",
    "_______\n|     |\n|     O\n|    /|\\\n|    /\n|\n|\n-------",
    "_______\n|     |\n|     O\n|    /|\\\n|    / \\\n|\n|\n-------"
]

# Initial game setup
word = choose_word()
guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = len(hangman_stages) - 1

# Hangman display
hangman_label = tk.Label(root, text=hangman_stages[0], font=("Courier", 16))
hangman_label.pack(pady=20)

# Word display
display_word = tk.StringVar()
update_display_word()
word_label = tk.Label(root, textvariable=display_word, font=("Courier", 24))
word_label.pack(pady=20)

# Entry widget for letter guessing
entry = tk.Entry(root, font=("Courier", 16))
entry.pack(pady=20)

# Guess button
guess_button = tk.Button(root, text="Guess", font=("Courier", 16), command=guess_letter)
guess_button.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Courier", 16), command=reset_game)
reset_button.pack(pady=10)

# Start the game loop
reset_game()
root.mainloop()
