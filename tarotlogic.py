import random

major = ["The Fool","The Magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","Strength","The Hermit","Wheel of Fortune","Justice","The Hanged Man","Death","Temperance","The Devil","The Tower","The Star","The Moon","The Sun","Judgement","The World"]
minorsuit = ["Swords","Wands","Cups","Pentacles"]
minorface = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Page","Knight","Queen","King"]
spreads = ["One Card", "One Card Major Arcana", "Daily Three Card", "Past Present Future", "Four Elemental Corners", "Five Card Crossroad", "Five Card Medium", "Pentagram", "Celtic Cross", "Zodiac Spread", ]

spreadlabels = [
    ["The Answer"], # One Card
    ["The Answer"], # One Major
    ["Energy of the Day", "What can I look forward to?", "What should I avoid?"], # Daily Three
    ["Past", "Present", "Future"], # PPF
    ["Air", "Fire", "Water", "Earth"], # Elements
    ["Present or Theme", "Past Influences", "Future", "Reason", "Potential"], # Crossroads
    ["The Deceased", "Message from the Deceased", "Important to the Deceased", "Deceased's State on the Other Side", "Communication from the Deceased in the Future"], # Medium
    ["The Question", "Spirit", "Fire", "Earth", "Air", "Water"], # Pentagram
    ["Present", "Immediate Challenge", "Distant Past", "Recent Past", "Best Outcome", "Immediate Future", "Your Influence", "External Influences", "Hopes and Fears", "Outcome"], # Celtic
    ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Theme"] # Zodiac
]

def get_fdeck(majoro=False):
    #full deck created, shuffled
    minorcards = [f"{f} of {s}" for s in minorsuit for f in minorface]
    deck = major[:]
    if not majoro:
        deck.extend(minorcards)
    random.shuffle(deck)
    return deck

def spreadpicker():
    for i, name in enumerate(spreads, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("\nSelect a spread [1-10]: ")) -1
        selected = spreads[choice]
        labels = spreadlabels[choice]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    #logic
    is_majoro = (choice == 1)
    deck = get_fdeck(majoro = is_majoro)

    print(f"\n--- {selected} ---")
    
    for label, card in zip(labels, deck):
        print(f"{label}: {card}")
    
if __name__ == "__main__":
    spreadpicker()

