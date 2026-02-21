import curses
from curses import wrapper
import queue
import time

maze = [
["█", "█", "O", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
["█", " ", " ", "█", " ", " ", " ", " ", " ", "█", " ", " ", " ", "█", " ", " ", " ", " ", " ", "█"],
["█", " ", "█", "█", " ", "█", "█", "█", "█", "█", " ", "█", " ", "█", "█", "█", " ", "█", " ", "█"],
["█", " ", " ", " ", " ", " ", " ", "█", " ", " ", " ", "█", " ", "█", " ", " ", " ", "█", " ", "█"],
["█", "█", "█", "█", "█", "█", " ", "█", " ", "█", "█", "█", " ", "█", "█", "█", " ", "█", " ", "█"],
["█", "█", " ", " ", " ", " ", " ", "█", " ", "█", " ", "█", " ", "█", " ", " ", " ", "█", " ", "█"],
["█", "█", " ", "█", "█", "█", "█", "█", " ", "█", " ", "█", " ", "█", " ", "█", "█", "█", " ", "█"],
["█", "█", " ", "█", " ", " ", " ", " ", " ", "█", " ", " ", " ", "█", " ", "█", " ", " ", " ", "█"],
["█", "█", " ", "█", " ", "█", "█", "█", "█", "█", " ", "█", "█", "█", " ", "█", "█", "█", " ", "█"],
["█", "█", " ", "█", " ", " ", " ", " ", " ", "█", " ", "█", " ", " ", " ", " ", " ", "█", " ", "█"],
["█", "█", " ", "█", "█", "█", "█", "█", " ", "█", " ", "█", " ", "█", "█", "█", "█", "█", " ", "█"],
["█", "█", " ", " ", " ", " ", " ", " ", " ", "█", " ", "█", " ", "█", " ", " ", " ", " ", " ", "█"],
["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", " ", "█", " ", "█", "█", "█", " ", "█", "█", "█"],
["█", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "█", " ", " ", " ", "█", " ", " ", " ", "█"],
["█", " ", "█", "█", "█", "█", "█", "█", " ", "█", "█", "█", "█", " ", "█", "█", " ", "█", " ", "█"],
["█", "█", " ", " ", " ", " ", " ", "█", " ", "█", " ", " ", " ", " ", " ", "█", " ", "█", " ", "█"],
["█", " ", " ", "█", "█", " ", "█", "█", " ", "█", "█", " ", "█", "█", "█", "█", " ", "█", " ", "█"],
["█", "█", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "█", " ", " ", " ", "█", " ", "█"],
["█", "█", " ", "█", "█", "█", "█", "█", "█", "█", "█", "█", " ", "█", "█", "█", " ", " ", "█", "█"],
["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "X", "█", "█"]
]

def printMaze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    GREEN =  curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j, "X", GREEN)
            else:
                stdscr.addstr(i, j, value, BLUE)

def findStart(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def findPath(maze, stdscr):
    start = "O"
    end = "X"
    startPOS = findStart(maze, start)

    q = queue.Queue()
    q.put((startPOS, [startPOS]))

    visited = set()

    while not q.empty():
        currentPOS, path = q.get()
        row, col = currentPOS

        stdscr.clear()
        printMaze(maze, stdscr, path)
        time.sleep(0.05)
        stdscr.refresh()
    
        if maze[row][col] == end:
            stdscr.addstr(21, 0, "Solved", curses.color_pair(2))
            return path

        neighbs = findNeighb(maze, row, col)
        for n in neighbs:
            if n in visited:
                continue

            r, c = n
            if maze[r][c] == "█":
                continue
            
            newPath = path + [n]
            q.put((n, newPath))
            visited.add(n)


def findNeighb(maze, row, col):
    neighbs = []

    if row > 0: #UP
        neighbs.append((row-1, col))
    if row + 1 < len(maze): #DOWN
        neighbs.append((row+1, col))
    if col > 0: #LEFT
        neighbs.append((row, col-1))
    if col + 1 < len(maze[0]): #RIGHT
        neighbs.append((row, col+1))
    
    return neighbs

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    findPath(maze, stdscr)
    stdscr.getch()
    
wrapper(main)