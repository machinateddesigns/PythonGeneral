from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)



def view():
    with open("pw.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip().split("|")
            user, pwd = data.split("|")

            print("Account:", user, "| Password:", fer.decrypt(pwd.encode()).decode())

def add():
    account = input("Account Name: ")
    pwd = input("Password: ")

    with open("pw.txt", "a") as f:
        f.write(account + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to view an existing password or add a new one? [view]/[add]. [q] to Quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")