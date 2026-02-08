import random

dicesides = 6

def roll(dicesides):
    dieroll = random.randint(1, dicesides)
    return dieroll

while True:
    players = input("Number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if players < 2 or players > 4:
            print("Must be between 2 and 4 players.")
        else:
            break
    else:
        print("Not a valid entry. Enter a number 2 through 4.")

max_score = 50

player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"Player {player_idx + 1}'s turn")
        print(f"Player {player_idx + 1} score is {player_scores[player_idx]} \n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (y) ")
            if should_roll.lower() != "y":
                print("\n")
                break
            value = roll(6)
            if value == 1:
                print("You rolled a one, turn done! \n")
                current_score = 0
                break
            else:
                print(f"You rolled a {value}!")
                current_score += value
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1} score is {player_scores[player_idx]}")


winner_score = max(player_scores)
winner = player_scores.index(winner_score) + 1
print(f"Player {winner} Won! Your score was {winner_score}! Congratulations!")