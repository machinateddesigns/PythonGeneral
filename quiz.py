print("Welcome to the Fallout Quiz!")
playing = input("Would you like to play? (y/n): ").lower()
if playing != 'y':
    print("Okie dokie! Goodbye!")
    quit()
print("Okie dokie! Let's play! ")

right = 0
score = 0

def correct(x):
    print("Correct!")
    global right
    right += 1
    global score
    score += x
def incorrect():
    print("Incorrect!")

if input("1. What vault do you start in, in Fallout 1? ") == "13":
    correct(1)
else:
    incorrect()

if input("2. What vault do you start in, in Fallout 3? ") == "101":
    correct(1)
else:
    incorrect()
    
if input("3. What vault do you start in, in Fallout 4? ") == "111":
    correct(1)
else:
    incorrect()

if input("4. What vault do you start in, in Fallout 76? ") == "76":
    correct(1)
else:
    incorrect()

if input("5. Where do you start in Fallout 2? ").lower() == "arroyo":
    correct(1)
else:
    incorrect()

if input("Bonus: What vault does Lucy McLane start in, in the Fallout TV series? ") == "33":
    correct(2)
else:
    incorrect()

print(f"You got {right} out of 6 questions correct, for a total of {score} points! That's {(score/7)*100}%")

quit()