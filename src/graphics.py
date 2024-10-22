from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__isRunning = False

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
