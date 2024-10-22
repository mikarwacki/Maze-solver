from graphics import Window, Line, Point 
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(10, 10,10,10,50,50,win)
    print("maze has been created")
    isSovled = maze.solve()
    if isSovled:
        print("THE MAZE HAS BEEN SOLVED")
    else:
        print("MAZE IS UNSOLVABLE")
    win.waitForClose()

main()