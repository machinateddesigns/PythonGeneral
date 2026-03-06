import random

def roll_dice(num_dice):
    """Simulates rolling a specified number of 6-sided dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def play_turn():
    """Manages the three rolls in a single turn."""
    kept_dice = []
    rolls_left = 3

    while rolls_left > 0:
        # Roll the remaining dice
        current_roll = roll_dice(5 - len(kept_dice))
        all_dice = sorted(kept_dice + current_roll)
        print(f"\nRoll {4 - rolls_left}: {all_dice}")
        
        if rolls_left == 1:
            # Last roll, forced to keep all
            print("Final roll. No more re-rolls possible.")
            break
        
        # Ask user which dice to keep
        keep_input = input("Which dice would you like to keep (e.g., '1,1,5')? Press Enter to re-roll all remaining: ")
        if not keep_input:
            continue
        
        try:
            # Convert input to a list of integers
            to_keep = [int(item) for item in keep_input.split(',')]
            
            # Simple validation (better validation needed for a full game)
            for die_val in to_keep:
                if die_val not in all_dice:
                    print(f"Error: {die_val} not in current roll. Try again.")
                    continue
            
            kept_dice = to_keep # This simple approach overwrites, a better approach manages a running list
            rolls_left -= 1

        except ValueError:
            print("Invalid input. Please use comma-separated numbers.")
    
    return all_dice

# Example of running a turn
if __name__ == "__main__":
    print("Starting a Yahtzee turn!")
    final_hand = play_turn()
    print(f"\nYour final hand: {final_hand}")
    # Next step: add scoring logic
