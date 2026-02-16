import random
import turtle
import time

WIDTH, HEIGHT = 500, 500
MIN_BET = 1
MAX_BET = 15

colors = []
speed = []
tNames = ['Shelly', 'Turbo', 'Franklin', 'Crush', 'Bowser', 'Donatello', 'Leonardo', 'Michaelangelo', 'Raphael', 'Squirtle', 'Oogway', 'Blastoise', 'Tortuga', 'Yertle', 'Kappa', 'Sheldon', 'Gamera', 'Aeschylus', 'Om', 'Atuin']
random.shuffle(tNames)

#randomize color function
def color():
    while True:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if r+g+b <= 650:
            break
    color = (r, g, b)
    return color

#randomize speed function
def rspeed():
    sp = random.randint(1, 10)
    return sp


def getNumTurtles():
    numTurtles = 0
    while True:
        numTurtles = input("How many turtles are racing today? (2-10) ")
        if numTurtles.isdigit():
            numTurtles = int(numTurtles)
        else:
            print("Invalid input. Try again.")
            continue
        if 2 <= numTurtles <= 10:
            return numTurtles
        else:
            print("Number is not between 2 and 10. Try again.")  

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtlesonic Racers")

racers = getNumTurtles()

for i in range(1, racers + 1):
    speed.append(int(rspeed()))
    colors.append(color())

init_turtle()
turtle.colormode(255)

def race():
    turtles = createTurtles()
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= (HEIGHT/2-25):
                return(turtles.index(racer)+1)
                #return tNames[turtles.index(racer)+1]
            
def createTurtles():
    turtles = []

    for i in range(1, racers + 1):

        racer = turtle.Turtle()
        racer.color(colors[i-1])
        racer.speed(speed[i-1])
        racer.shape('turtle')
        racer.penup()
        #set postion
        #racer.setpos(((-WIDTH/2)*((2*i-1)/racers))+(WIDTH/2),((-HEIGHT)/2)+25)
        racer.setpos(((WIDTH/2)*((2*i-1)/racers))-(WIDTH/2),((-HEIGHT)/2)+10)
        racer.pendown()
        racer.left(90)
        racer.write(f"{i} {tNames[i]}", move=False, align="center", font=("Arial", 8,"normal"))
        racer.penup()
        racer.forward(20)
        racer.pendown()
        turtles.append(racer)
        #print(f"{i} {tNames[i]}{((-WIDTH/2)*((2*i-1)/racers))+(WIDTH/2),((-HEIGHT)/2)+25}")
    return turtles

def deposit():
    while True:
        amount = input("Insert Coin. How many coins do you insert? ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 1:
                break
            else:
                print("Must be a whole number greater than 0.")
        else:
            print("Please enter a whole number.")
    return amount

def get_bet(balance):
    while True:
        amount = input(f"How much do you want to bet? (1-15) ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                if amount <= balance:
                    balance -= amount
                    print(f"Bet: {amount} coins. New balance: {balance} coins.")
                    break
                else:
                    print("You don't have enough coins to bet that amount.")
                    print(f"Your current balance is {balance}")
                    addbal = input("Do you want to insert more coins? (y/q to quit)").lower()
                    if addbal == "y":
                        balance += deposit()
                        print(f"New balance: {balance} coins.")
                    if addbal == 'q':
                        quit()
            else:
                print(f"Must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a whole number.")
    return amount, balance

def guessing():
    while True:
        guess = input(f"Which number turtle are you betting on? ")
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Invalid input. Try again.")
            continue
        if 1 <= guess <= racers:
            return guess
        else:
            print(f"Number is not between 1 and {racers}. Try again.")  

def event(balance, racers):
    while True:
        for n in range(racers, 0, -1):
            print(f"Turtle {(n)}: {tNames[n]}")
        bet = get_bet(balance)
        guess = guessing()
        balance = bet[1]
        print(f"You bet on {tNames[guess]}")
        #turtle.clearscreen()
        winner = race()
        print(f"{tNames[winner]} won the race!")
        if winner == guess:
            again = input(f"Your turtle, {tNames[guess]} won! You win {bet[0]*racers} coins! Play again? (y)").lower()
            balance += bet[0]*racers
        else:
            again = input(f"Your turtle, {tNames[guess]}, didn't win. Better luck next time. Play again? (y)").lower()
        if again != 'y':
            break
        else: 
            turtle.clearscreen()
            turtle.colormode(255)
balance = deposit()
event(balance, racers)
time.sleep(1)