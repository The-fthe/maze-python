import unittest
from maze import Maze
from cell import Cell


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_last_cell_pos(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        last_cell = m1.cells[m1.num_cols-1][m1.num_rows-1]
        self.assertEqual(isinstance(last_cell, Cell), True)
        self.assertEqual(
            last_cell._x1,
            m1.x1 + (m1.num_cols-1) * m1.cell_size_x
        )
        self.assertEqual(
            last_cell._y1,
            m1.y1 + (m1.num_rows-1) * m1.cell_size_y
        )


if __name__ == "__main__":
    unittest.main()
