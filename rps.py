import random

user_wins = 0
computer_wins = 0
choices=["r", "p", "s"]

while True:
    user_input = input("Enter [r]ock, [p]aper, or [s]cissors (or [q] to stop playing): ").lower()
    if user_input == "q":
        break
    if user_input not in choices:
        print("Invalid choice, please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "r" and computer_choice == "s") or \
         (user_input == "p" and computer_choice == "r") or \
         (user_input == "s" and computer_choice == "p"):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

print(f"Final Score - You: {user_wins}, Computer: {computer_wins}")