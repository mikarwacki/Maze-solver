from graphics import Window, Line, Point 
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(10, 10,10,10,50,50,win,10)
    win.waitForClose()

main()