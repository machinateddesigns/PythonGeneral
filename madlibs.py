from pathlib import Path

storypath = Path("d:/github/python/pythongeneral/stories/story.txt")

with open(storypath, "r") as f:
    story = f.read()

words = set()
startWord = -1
targetStart = "<"
targetEnd = ">"

for i, char in enumerate(story):
    if char == targetStart:
        startWord = i

    if char == targetEnd and startWord != -1:
        word = story[startWord: i + 1]
        words.add(word)
        startWord = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
