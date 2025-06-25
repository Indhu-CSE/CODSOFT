import random
import tkinter as tk
from tkinter import messagebox

# Game logic to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

# Exit confirmation
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit the game?"):
        window.destroy()

# GUI Setup
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")

user_score = 0
computer_score = 0

tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack()

rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=20)

score_label = tk.Label(window, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
