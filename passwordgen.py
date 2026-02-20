import random
import string

from cryptography.fernet import Fernet

def genPassword(minLength, lower=True, upper=True, number=True, specialchar=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    characters = letters
    if number:
        characters += digits
    if specialchar:
        characters += special

    pwd = ""
    meetsCriteria = False
    hasNum = False
    hasSpecial = False
    hasLower = False
    hasUpper = False

    while not meetsCriteria or len(pwd) < minLength:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in lower:
            hasLower = True
        elif newChar in upper:
            hasUpper = True
        elif newChar in digits:
            hasNum = True
        elif newChar in special:
            hasSpecial = True
        
        meetsCriteria = True
        if lower:
            meetsCriteria = hasLower
        if upper:
            meetsCriteria = hasUpper and hasLower
        if number:
            meetsCriteria = hasNum and hasUpper and hasLower
        if special:
            meetsCriteria = hasSpecial and hasNum and hasUpper and hasLower

    return pwd

print("Password will contain uppercase, lowercase, numbers, and special characters. We are not compromising security.")
minLength = int(input("Enter the minimum length: "))

pwd = genPassword(minLength)
print(f"The generated password is: {pwd}")