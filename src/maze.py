from graphics import Point, Window
from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._createCells()
        self._breakEntranceAndExit()
        self._breakWallsR(0, 0)
        self._resetCellsVisited()

    def _createCells(self):
        for i in range(self.num_cols):
            temp = []
            for j in range(self.num_rows):
                temp.append(Cell(self.win))
            self._cells.append(temp)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02)

    def _breakEntranceAndExit(self):
        self._cells[0][0].hasTopWall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].hasBottomWall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _breakWallsR(self, i, j):
        self._cells[i][j].visited = True

        while True:
            toVisit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                toVisit.append((i - 1, j))

            if i + 1 < len(self._cells) and not self._cells[i + 1][j].visited:
                toVisit.append((i + 1, j))

            if j > 0 and not self._cells[i][j-1].visited:
                toVisit.append((i, j - 1))

            if j + 1 < len(self._cells[i]) and not self._cells[i][j + 1].visited:
                toVisit.append((i, j + 1))

            if len(toVisit) == 0:
                self._draw_cell(i, j)
                return

            idx = random.randrange(len(toVisit))
            direction = toVisit[idx]
            if direction[0] == i - 1:
                self._cells[direction[0]][direction[1]].hasRightWall = False
                self._cells[i][j].hasLeftWall = False

            if direction[0] == i + 1:
                self._cells[direction[0]][direction[1]].hasLeftWall = False
                self._cells[i][j].hasRightWall = False

            if direction[1] == j - 1:
                self._cells[direction[0]][direction[1]].hasBottomWall = False
                self._cells[i][j].hasTopWall = False

            if direction[1] == j + 1:
                self._cells[direction[0]][direction[1]].hasTopWall = False
                self._cells[i][j].hasBottomWall = False

            self._breakWallsR(direction[0], direction[1])
            
    def _resetCellsVisited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
