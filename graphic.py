from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2,
                           self.y2, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width: float, height: float):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="grey",
                             height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__root.running = True
        while self.__root.running:
            self.redraw()
        print("window closed..")

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, "black")

    def close(self):
        self.__running = False
