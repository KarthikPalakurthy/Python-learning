import random

print("Let's Play Rock, Paper, Scissors !!!!")

choice = input("Make your move: ").lower()

cpu_options = ["rock", "paper", "scissors"]

cpu_choice = random.choice(cpu_options)

print(f"Computer plays {cpu_choice}")

if choice == cpu_choice:
    print("It's a draw!!!")
elif choice == "rock":
    if cpu_choice == "paper":
        print("CPU Wins!!!")
    elif cpu_choice == "scissors":
        print("Player Wins!!!")
elif choice == "paper":
    if cpu_choice == "scissors":
        print("CPU Wins!!!")
    elif cpu_choice == "rock":
        print("Player Wins!!!")
elif choice == "scissors":
    if cpu_choice == "rock":
        print("CPU Wins!!!")
    elif cpu_choice == "paper":
        print("Player Wins!!!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
