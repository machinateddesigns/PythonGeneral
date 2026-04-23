import random

set = ["major", "minor"]
major = ["The Fool","The Magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","Strength","The Hermit","Wheel of Fortune","Justice","The Hanged Man","Death","Temperance","The Devil","The Tower","The Star","The Moon","The Sun","Judgement","The World"]
minorsuit = ["Swords","Wands","Cups","Pentacles"]
minorface = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Page","Knight","Queen","King"]

'''
#loops example
for s in set:
    if s == "major":
        for m in major:
            #print(m)
    else:
        for m in minorsuit:
            for f in minorface:
                #print(f, "of", m)
'''

s = random.choice(set)
card = ""
if s == "major":
    card = random.choice(major)
    print("Your card is", card)
else:
    suit = random.choice(minorsuit)
    face = random.choice(minorface)
    print("Your card is the", face, "of", suit)