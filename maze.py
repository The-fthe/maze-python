from cell import Cell
from graphic import Point
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.create_cells()
        pass

    def create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self.cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i, j)
        pass

    def draw_cell(self, i, j) -> Point:
        if self.win is None:
            print("win is None")
            return
        c = Cell(self.win)
        p_1 = Point(self.x1 + i * self.cell_size_x,
                    self.y1 + j * self.cell_size_y)
        p_2 = Point(p_1.x + self.cell_size_x, p_1.y + self.cell_size_y)
        self.cells[i][j].draw(p_1, p_2)
        self.animate()
        pass

    def animate(self):
        if self.win is None:
            print("win is None")
            return
        time.sleep(0.05)
        self.win.redraw()
        pass
