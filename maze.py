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

        random.seed = 1
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_wall_r(0, 0)
        self._reset_cell_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self.draw_move(i, j)

    def draw_move(self, i, j):
        p_1 = Point(self._x1 + i * self._cell_size_x,
                    self._y1 + j * self._cell_size_y)
        p_2 = Point(p_1.x + self._cell_size_x, p_1.y + self._cell_size_y)
        self._cells[i][j].draw(p_1, p_2)
        # self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_up_wall = False
        self.draw_move(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_down_wall = False
        self.draw_move(self._num_cols-1, self._num_rows-1)
        pass

    def _break_wall_r(self, i, j):
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        while True:
            neighbors = []
            # Check left neighbor
            if i > 0 and not self._cells[i-1][j].visited:
                neighbors.append((i-1, j))
            # Check right neighbor
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                neighbors.append((i+1, j))
            # Check up neighbor
            if j > 0 and not self._cells[i][j-1].visited:
                neighbors.append((i, j-1))
            # Check down neighbor
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                neighbors.append((i, j+1))

            if len(neighbors) == 0:
                self.draw_move(i, j)
                return

            move_index = random.randrange(len(neighbors))
            x, y = neighbors[move_index]
            # x, y = neighbors[0]
            # right
            if x == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if x == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if y == j + 1:
                self._cells[i][j].has_down_wall = False
                self._cells[i][j+1].has_up_wall = False
            # up
            if y == j - 1:
                self._cells[i][j].has_up_wall = False
                self._cells[i][j-1].has_down_wall = False

            self._break_wall_r(x, y)

    def _reset_cell_visited(self, value=False):
        for cols in self._cells:
            for row in cols:
                row.visited = value

    def solve(self):
        is_solve = self._solve_r(0, 0)
        if is_solve:
            end_cell = self._cells[self._num_cols-1][self._num_rows-1]
            x_mid = (end_cell._x1 + end_cell._x2) / 2
            y_mid = (end_cell._y1 + end_cell._y2) / 2
            x_down_mid = x_mid
            y_down_mid = y_mid + (end_cell._y2 - end_cell._y1)/2
            end_cell.draw(Point(x_mid, y_mid), Point(
                x_down_mid, y_down_mid), "green")
        return is_solve

    def _solve_r(self, i, j):
        self._animate()
        curr_cell = self._cells[i][j]
        curr_cell.visited = True
        end_cell = self._cells[self._num_cols-1][self._num_rows-1]
        # if curr_cell == end_cell:
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        is_exit = False
        # Check left neighbors
        if i > 0 and not self._cells[i-1][j].visited and not curr_cell.has_left_wall:
            curr_cell.draw_move(self._cells[i-1][j])
            is_exit = self._solve_r(i-1, j)
            if is_exit:
                return is_exit
            curr_cell.draw_move(self._cells[i-1][j], True)
        # Check right neighbor
        if i < self._num_cols-1 and not self._cells[i+1][j].visited and not curr_cell.has_right_wall:
            curr_cell.draw_move(self._cells[i+1][j])
            is_exit = self._solve_r(i+1, j)
            if is_exit:
                return is_exit
            curr_cell.draw_move(self._cells[i+1][j], True)
        # Check up neighbor
        if j > 0 and not self._cells[i][j-1].visited and not curr_cell.has_up_wall:
            curr_cell.draw_move(self._cells[i][j-1])
            is_exit = self._solve_r(i, j-1)
            if is_exit:
                return is_exit
            curr_cell.draw_move(self._cells[i][j-1], True)
        # Check down neighbor
        if j < self._num_rows-1 and not self._cells[i][j+1].visited and not curr_cell.has_down_wall:
            curr_cell.draw_move(self._cells[i][j+1])
            is_exit = self._solve_r(i, j+1)
            if is_exit:
                return is_exit
            curr_cell.draw_move(self._cells[i][j+1], True)
        if not is_exit:
            return False
