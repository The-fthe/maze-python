from graphic import Window, Point
from cell import Cell
from maze import Maze


def main():
    num_rows = 10
    num_cols = 8
    offset = 100
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * offset) / num_cols
    cell_size_y = (screen_y - 2 * offset) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(offset, offset, num_rows, num_cols,
                cell_size_x, cell_size_y, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
