from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.hasLeftWall = True 
        self.hasRightWall = True
        self.hasTopWall = True 
        self.hasBottomWall = True 
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.hasLeftWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.hasRightWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")

        line = Line(Point(x1, y1), Point(x2, y1))
        if self.hasTopWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")
        
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.hasBottomWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")


    def drawMove(self, to_cell, undo=False):
        c1 = Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)
        c2 = Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)
        color = "grey" if undo else "red"
        self._win.drawLine(Line(c1,c2), fillColor=color)
    