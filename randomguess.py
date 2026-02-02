import random

global dicesides

while True:

    dicesides = input("How many sides should the die have? ")
    if dicesides.isdigit():
        dicesides = int(dicesides)
        if dicesides >= 2:
            break
        else:
            print("The die must have at least 2 sides, try again.")
    else:
        print("Please enter a number")

print(f"Roll a d{dicesides} {(random.randint(1, dicesides))}")

print("Now that we have rolled the die, try to guess the number!")

dieroll = random.randint(1, dicesides)
guesses = 0

while True:
    guess = input(f"Enter your guess between 1 and {dicesides}: ")
    guesses += 1
    if guess.isdigit():
        guess = int(guess)
        if guess > dicesides or guess < 1:
            print("Your guess is not even on the die! Try again.")
        elif guess == dieroll:
            print(f"You did it! You guessed the number on the die! It took you {guesses} guess(es).")
            break
        else:
            if guess < dieroll:
                print("Sorry, that was too low. Try again!")
            else:
                print("Sorry, that was too high. Try again!")
    else:
        print("Please enter a valid number.")
    
        
            