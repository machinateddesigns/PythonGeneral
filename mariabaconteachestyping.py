import curses
from curses import wrapper
import time
import random
file_path = "typingtext.txt"
with open(file_path, 'r') as f:
    content = f.read()
    lines = content.splitlines()
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to Maria Bacon Teaches Typing! ⌨️")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
def display_text(stdscr, target, current, mistakes, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"Mistakes: {mistakes}")
    stdscr.addstr(2, 0, f"WPM: {wpm}")
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
def wpm_test(stdscr):
    target_text = lines[random.randrange(0, 20)]
    current_text = []
    wpm = 0
    mistakes = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        stdscr.clear()
        display_text(stdscr, target_text, current_text, mistakes, wpm)
        stdscr.refresh()
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            return time_elapsed, wpm, mistakes, len(target_text)
        try: key = stdscr.getkey()
        except: continue
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            if key != target_text[len(current_text)]:
                mistakes += 1
            current_text.append(key)
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
        output = []
        output = wpm_test(stdscr)
        output[2]
        stdscr.addstr(3, 0, f"Congratulations! You typed out the sentence with only {output[2]} mistakes,")
        stdscr.addstr(4, 0, f"and an accuracy of {round((int(output[3])-int(output[2]))/int(output[3])*100)}% in {round(output[0])} seconds, giving you a WPM of {output[1]}. Good job!")
        stdscr.addstr(5, 0, f"Would you like to play again? (any key to continue, [esc] to end) ")
        end = stdscr.getkey()
        if ord(end) == 27:
            break
wrapper(main)