import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    # Update the labels with user and computer choices
    user_choice_label.config(text="You chose: " + user_choice)
    computer_choice_label.config(text="Computer chose: " + computer_choice)
    
    # Determine the game result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
        update_score('user')
    else:
        result = "You lose!"
        update_score('computer')
    
    result_label.config(text="Result: " + result)

# Function to update scores
def update_score(winner):
    global user_score, computer_score
    if winner == 'user':
        user_score += 1
    else:
        computer_score += 1
    
    user_score_label.config(text="Your Score: " + str(user_score))
    computer_score_label.config(text="Computer Score: " + str(computer_score))

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="Result: ")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Initialize the user and computer scores
user_score = 0
computer_score = 0

# Create the labels and buttons for the GUI
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
instruction_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: determine_winner("Rock"))
rock_button.grid(row=1, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: determine_winner("Paper"))
paper_button.grid(row=1, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=1, column=2, padx=10, pady=10)

user_choice_label = tk.Label(root, text="You chose: ")
user_choice_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

computer_choice_label = tk.Label(root, text="Computer chose: ")
computer_choice_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

user_score_label = tk.Label(root, text="Your Score: 0")
user_score_label.grid(row=5, column=0, padx=10, pady=10)

computer_score_label = tk.Label(root, text="Computer Score: 0")
computer_score_label.grid(row=5, column=2, padx=10, pady=10)

# Reset button to restart the game
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
