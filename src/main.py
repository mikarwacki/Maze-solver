from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    # cell = Cell(Point(10,10), Point(50,50), win)
    # cell2 = Cell(Point(10,50), Point(50,90), win)
    # cell.draw()
    # cell2.draw()
    # cell.drawMove(cell2)
    maze = Maze(10, 10,15,15,50,50,win)
    win.waitForClose()

main()