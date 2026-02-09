import random
import math

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 15

ROWS = 3
COLS = 3

symbol_count = {
    "🃏": 1,
    "♠️": 1,
    "🏆": 1,
    "💎": 1,
    "👑": 1,
    "💲": 1,
    "🍎": 2,
    "🍇": 2,
    "🍊": 2,
    "🍋": 3,
    "🍒": 4
}

symbol_value = {
    "🃏": 10,
    "♠️": 5,
    "🏆": 4.5,
    "💎": 4,
    "👑": 3.5,
    "💲": 3,
    "🍎": 2.5,
    "🍇": 2,
    "🍊": 1.75,
    "🍋": 1.5,
    "🍒": 1.25
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    if winnings != 0:
        print(f"You won {winnings}!")
    return winnings

def get_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end = " | ")
                else:
                    print(column[row])

def deposit():
    print("Payouts: ")
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

def get_bet():
    while True:
        amount = input(f"What would you like to bet? 1=1 line, 4=2 lines, 9=3. Max {MAX_BET} coins. ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a whole number.")
    return amount

def game_loop(balance):
    while True:
        bet = get_bet()
        if bet > balance:
            print("You don't have enough coins to bet that amount.")
            print(f"Your current balance is {balance}")
        else:
            balance -= bet
            break

    num_lines = math.floor(math.sqrt(bet))
    print(balance, bet, num_lines)
    print(f"You are betting {bet} on {num_lines} lines.")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    balance += check_winnings(slots, num_lines, bet, symbol_value)
    input(f"Remaining balance: {balance}. Play again?")

def main():
    balance = deposit()
    while True:
        play = input(f"Press enter to play, or enter (q) to quit").lower()
        if play != "q":
            game_loop(balance)
        else:
            break
main()