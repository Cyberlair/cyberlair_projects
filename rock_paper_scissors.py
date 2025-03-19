import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice (rock, paper, scissors) or 'q' to quit.")

while True:
    user_choice = input("Your choice: ").strip().lower()
    if user_choice == 'q':
        print("Exiting game...")
        break

    if user_choice not in options:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    print("Play again? (y/n)")
    play_again = input().strip().lower()
    if play_again != 'y':
        print("Exiting game...")
        break