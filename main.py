from graphic import Window
from maze import Maze


def main():
    num_rows = 20
    num_cols = 15
    offset = 100
    screen_x = 800
    screen_y = 700
    cell_size_x = (screen_x - 2 * offset) / num_cols
    cell_size_y = (screen_y - 2 * offset) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(offset, offset, num_rows, num_cols,
                cell_size_x, cell_size_y, win)
    result = maze.solve()
    print(f"solve:{result}")
    win.wait_for_close()


if __name__ == "__main__":
    main()
