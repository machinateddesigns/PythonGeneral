import random

spheres = ['correspondence', 'entropy', 'forces', 'life', 'matter', 'mind', 'prime', 'spirit', 'time']
available_spheres = spheres.copy()

mage_types_lib = {"Chronomancer": ["Time", "Spirit", "Prime"], "Prophet": ["Time", "Spirit", "Mind"], "Relic Keeper": ["Time", "Spirit", "Matter"], "Cycle Warden": ["Time", "Spirit", "Life"], "Storm Shaman": ["Time", "Spirit", "Forces"], "Doom Prophet": ["Time", "Spirit", "Entropy"], "Spirit Traveller": ["Time", "Spirit", "Correspondence"], "Akashic": ["Time", "Prime", "Mind"], "Alchemist": ["Time", "Prime", "Matter"], "Immortal Adept": ["Time", "Prime", "Life"], "Energy Worker": ["Time", "Prime", "Forces"], "Fateweaver": ["Time", "Prime", "Entropy"], "Dimensional Voyager": ["Time", "Prime", "Correspondence"], "Artificer": ["Time", "Mind", "Matter"], "Reincarnation Mystic": ["Time", "Mind", "Life"], "Battle Seer": ["Time", "Mind", "Forces"], "Paradox Seer": ["Time", "Mind", "Entropy"], "Traveller": ["Time", "Mind", "Correspondence"], "Biomancer": ["Time", "Matter", "Life"], "Golem Crafter": ["Time", "Matter", "Forces"], "Rust Witch": ["Time", "Matter", "Entropy"], "Shaper": ["Time", "Matter", "Correspondence"], "Evolutionist": ["Time", "Life", "Forces"], "Thanaturge": ["Time", "Life", "Entropy"], "Lineage Seer": ["Time", "Life", "Correspondence"], "Cataclysm Mage": ["Time", "Forces", "Entropy"], "Chrono-Evoker": ["Time", "Forces", "Correspondence"], "Fate Oracle": ["Time", "Entropy", "Correspondence"], "Gnostic Mystic": ["Spirit", "Prime", "Mind"], "Relic Forger": ["Spirit", "Prime", "Matter"], "Faith Healer": ["Spirit", "Prime", "Life"], "Evocationist": ["Spirit", "Prime", "Forces"], "Karmic Judge": ["Spirit", "Prime", "Entropy"], "Gatekeeper": ["Spirit", "Prime", "Correspondence"], "Fetish Witch": ["Spirit", "Mind", "Matter"], "Vision Healer": ["Spirit", "Mind", "Life"], "Ecstatic": ["Spirit", "Mind", "Forces"], "Mad Oracle": ["Spirit", "Mind", "Entropy"], "Spirit Medium": ["Spirit", "Mind", "Correspondence"], "Fleshcrafter": ["Spirit", "Matter", "Life"], "Totem Mage": ["Spirit", "Matter", "Forces"], "Bone Hag": ["Spirit", "Matter", "Entropy"], "Idol Maker": ["Spirit", "Matter", "Correspondence"], "Druid": ["Spirit", "Life", "Forces"], "Psychopomp": ["Spirit", "Life", "Entropy"], "Spirit Guide": ["Spirit", "Life", "Correspondence"], "Exorcist": ["Spirit", "Forces", "Entropy"], "Thunder Shaman": ["Spirit", "Forces", "Correspondence"], "Grave Walker": ["Spirit", "Entropy", "Correspondence"], "Thaumaturge": ["Prime", "Mind", "Matter"], "Willworker": ["Prime", "Mind", "Life"], "Energy Adept": ["Prime", "Mind", "Forces"], "Probability Mage": ["Prime", "Mind", "Entropy"], "Mentalist": ["Prime", "Mind", "Correspondence"], "Master Alchemist": ["Prime", "Matter", "Life"], "Runesmith": ["Prime", "Matter", "Forces"], "Void Alchemist": ["Prime", "Matter", "Entropy"], "Ley Architect": ["Prime", "Matter", "Correspondence"], "Vitalist": ["Prime", "Life", "Forces"], "Resurrectionist": ["Prime", "Life", "Entropy"], "Sacred Heir": ["Prime", "Life", "Correspondence"], "Annihilator": ["Prime", "Forces", "Entropy"], "Star Mage": ["Prime", "Forces", "Correspondence"], "Singularity Mystic": ["Prime", "Entropy", "Correspondence"], "Psychobiologist": ["Mind", "Matter", "Life"], "Psychokinetic": ["Mind", "Matter", "Forces"], "Obsession Witch": ["Mind", "Matter", "Entropy"], "Remote Operator": ["Mind", "Matter", "Correspondence"], "Monk": ["Mind", "Life", "Forces"], "Trauma Eater": ["Mind", "Life", "Entropy"], "Empath": ["Mind", "Life", "Correspondence"], "Stress Mage": ["Mind", "Forces", "Entropy"], "Telekinetic": ["Mind", "Forces", "Correspondence"], "Conspiracy Seer": ["Mind", "Entropy", "Correspondence"], "Golemancer": ["Matter", "Life", "Forces"], "Plague Witch": ["Matter", "Life", "Entropy"], "Body Shaper": ["Matter", "Life", "Correspondence"], "Demolitions Mage": ["Matter", "Forces", "Entropy"], "Weaponsmith": ["Matter", "Forces", "Correspondence"], "Salvage Mage": ["Matter", "Entropy", "Correspondence"], "Apex Predator": ["Life", "Forces", "Entropy"], "Beastmaster": ["Life", "Forces", "Correspondence"], "Extinction Seer": ["Life", "Entropy", "Correspondence"], "Disaster Mage": ["Forces", "Entropy", "Correspondence"]}

start = input("Welcome to Witch City Salem! Do you want to play? (y/n) ")
if start.lower() != 'y':
    print("Maybe next time! Goodbye.")
    exit()
print("Your adventure begins now.")
name = input("What is your name? ")

magictype1 = "none"
magictype2 = "none"
magictype3 = "none"

'''
validate the input against the spheres list
'''
while magictype1.lower() not in available_spheres:
    magictype1 = input(f"{name}, choose your first magic type: {'[' + '],['.join(available_spheres) + ']'} ").lower()
    if magictype1.lower() not in available_spheres:
        print("That's not one of the available spheres. Please try again.")
        continue
#remove chosen sphere from the list but keep the original list intact for future use
available_spheres.remove(magictype1.lower())


while magictype2.lower() not in available_spheres:
    magictype2 = input(f"{name}, choose your second magic type: {'[' + '],['.join(available_spheres) + ']'} ").lower()
    if magictype2.lower() not in available_spheres:
        print("That's not one of the available spheres. Please try again.")
        continue
#remove chosen sphere from the list but keep the original list intact for future use
available_spheres.remove(magictype2.lower())

while magictype3.lower() not in available_spheres:
    magictype3 = input(f"{name}, choose your third magic type: {'[' + '],['.join(available_spheres) + ']'} ").lower()
    if magictype3.lower() not in available_spheres:
        print("That's not one of the available spheres. Please try again.")
        continue
#remove chosen sphere from the list but keep the original list intact for future use
available_spheres.remove(magictype3.lower())

print(f"Great! {name}, you have chosen {magictype1.title()}, {magictype2.title()}, and {magictype3.title()} as your spheres of magic.")

# determine mage type based on the chosen spheres, order does not matter.
chosen_spheres = sorted([magictype1, magictype2, magictype3])
magetype = "Orphan Mage"
for mtype, spheres in mage_types_lib.items():
    if sorted([s.lower() for s in spheres]) == chosen_spheres:
        magetype = mtype
        break

print(f"Based on your chosen spheres, your mage type is: {magetype}.")
print("Good Luck on your magical journey!")

print('''You arrive at the Chantry on Water Street, away from the prying eyes of tourists and locals.
An ornately carved wood and glass door stands at the entrance to the Chantry. You try and
remember the password to get in...''')
password = input("What is the password to enter the chantry? ").lower()

print(f'''That's right {name}, the password is '{password.title()}'. The door unlocks, and you step inside.
Inside, the Chantry is dimly lit with candles and filled with the scent of musty books and pleasant herbs.
A man approaches you, one of the acolytes of the Chantry. He offers to take your coat and make you a cup of tea.''')
tea_type = input("Would you like herbal, green, or black tea? ").lower()

if tea_type in ['green', 'black']:
    print(f'''The acolyte nods and prepares a cup of {tea_type} tea for you. As you sip the tea, you feel the rush of
magic and caffeine coursing through your veins. You are ready to meet with the Archmage now.
You head to the headmaster's office, located at the top of the Wizard's Tower. The door is guarded by an ancient raven.
The raven eyes you suspiciously, and says "Right, we've got that newfangled multi-factor-authentication system now. 
Using magic, determine what number I'm thinking of between 1 and 10, then tell me so I can let you in."''')
    mfa_number = random.randint(1, 10)
    sphereuse = input("What sphere do you use to determine the number? ").lower()
    if sphereuse in [magictype1, magictype2, magictype3]:
        print(f'''You focus your {sphereuse.title()} magic and divine that the raven is thinking of the number {mfa_number}.
You say to the raven, "The number you're thinking of is {mfa_number}." The raven ruffles his feathers and
jumps through a little hole in the wall, unlocking the door from the other side. It slowly swings open for you.
Inside, you see a room filled with ancient tomes, equiptment, paraphenalia, a large hearth, and the Archmage,
seated behind an enormous mahogany desk, stacked high with papers and books. He appears to be brewing something
as you enter, and with a dramatic 'FWOOSH!' it erupts in a colorful plume of smoke and sparks. He looks up at
you and says, "Caught me in the middle of lunch, you have. Alchemy dulls the taste buds, you see, so I put Jenkin's
WOW WOW sauce on just about everything to spice it up. Care for a taste?"''')
        alchemy_choice = input("Do you want to try the Archmage's concoction? (y/n) ").lower()
        if alchemy_choice == 'y':
                print(f'''You take a spoonful of the soupy concoction. The flavors explode in your mouth, literally, as the WOW WOW sauce
transfoms your entire body into cinders and ash. You have met a fiery end, {name}. Game Over.''')
        else:
            print(f'''Erring on the side of caution, you politely decline the Archmage's offer. He nods in understanding, and
offers you a seat by his desk. "Probably for the best," he chuckles. "WOW WOW Sauce isn't for the faint of heart."
You spend the afternoon discussing magical theory, the history of the city, and your next assignment, to recover
an artifact lost or stolen from the nearby cemetary, the skeleton of the famous witch Tituba. You leave the Chantry
feeling enlightened and ready to tackle this problem. You head to your quarters to grab your gear and prepare for the task ahead.
                      
That is the end of this section of the adventure. More to come later!''')
    else:
        print(f'''You attempt to use {sphereuse.title()} magic to divine the number, but alas, you don't know that sphere of magic.
Witless and confused, you guess 13. The raven caws loudly, transforming into a fearsome dragon, incinerating you where you stand.
Game Over.''')    

else:
    print(f'''You drink the concoction and immediately regret it. Moments later, you lie dead on the floor. Game Over.''')