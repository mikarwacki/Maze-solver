from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Title"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def waitForClose(self):
        self.__isRunning = True
        while self.__isRunning:
            self.redraw()
        print("windows closed...")
    
    def close(self):
        self.__isRunning = False

    def drawLine(self, line, fillColor="black"):
        line.draw(self.__canvas, fillColor)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fillColor="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fillColor, width=2)

class Cell:
    def __init__(self, p1, p2, window):
        self.hasLeftWall = True 
        self.hasRightWall = True
        self.hasTopWall = True 
        self.hasBottomWall = True 
        self.visited = False
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self._win = window

    def draw(self):
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.hasLeftWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")

        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.hasRightWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")

        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.hasTopWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")
        
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.hasBottomWall:
            self._win.drawLine(line)
        else:
            self._win.drawLine(line, "white")


    def drawMove(self, to_cell, undo=False):
        c1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        c2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        color = "grey" if undo else "red"
        self._win.drawLine(Line(c1,c2), fillColor=color)
    
    def printWalls(self):
        print(f"top: {self.hasTopWall}, bottom: {self.hasBottomWall}, left: {self.hasLeftWall}, right: {self.hasRightWall}")