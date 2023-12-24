from cell import Cell
from graphic import Point
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        # win none for unittest
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._seed = 1
        random.seed = self._seed

        self._create_cells()
        self._break_entrance_and_exit()
        rand_col = random.randint(0, self._num_cols-1)
        rand_row = random.randint(0, self._num_rows-1)
        self._break_wall_r(rand_col, rand_row)

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        p_1 = Point(self._x1 + i * self._cell_size_x,
                    self._y1 + j * self._cell_size_y)
        p_2 = Point(p_1.x + self._cell_size_x, p_1.y + self._cell_size_y)
        self._cells[i][j].draw(p_1, p_2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_down_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)
        pass

    def _break_wall_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        while True:
            neighbors = []
            # Check right neighbor
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                neighbors.append(("right", i, j + 1))
            # Check left neighbor
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                neighbors.append(("left", i, j - 1))
            # Check down neighbor
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                neighbors.append(("down", i + 1, j))
            # Check up neighbor
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                neighbors.append(("up", i - 1, j))

            if len(neighbors) == 0:
                self._draw_cell(i, j)
                break
            else:
                move_index = random.randint(0, len(neighbors)-1)
                (direction, x, y) = neighbors[move_index]
                if direction == "left":
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j)
                    self._cells[x][y].has_left_wall = False
                    self._draw_cell(x, y)
                    pass
                elif direction == "right":
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j)
                    self._cells[x][y].has_right_wall = False
                    self._draw_cell(x, y)
                    pass
                elif direction == "up":
                    self._cells[i][j].has_up_wall = False
                    self._draw_cell(i, j)
                    self._cells[x][y].has_down_wall = False
                    self._draw_cell(x, y)
                    pass
                elif direction == "down":
                    self._cells[i][j].has_down_wall = False
                    self._draw_cell(i, j)
                    self._cells[x][y].has_up_wall = False
                    self._draw_cell(x, y)
                    pass
                self._break_wall_r(x, y)

        pass
