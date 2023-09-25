import random
import time


choices = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
computer_choice = random.choice(choices)

print(f"You chose {user_choice}.")
print(f"The computer chose {computer_choice}.")

time.sleep(1)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {user_choice}.")