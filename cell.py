from graphic import Window, Point, Line


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_down_wall = True
        self.is_visited = False
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = win

    def draw(self, p1: Point, p2: Point):
        fill_color = "black"
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        # left
        left_l = Line(Point(p1.x, p1.y), Point(p1.x, p2.y))
        # right
        right_l = Line(Point(p2.x, p1.y), Point(p2.x, p2.y))
        # top
        top_l = Line(Point(p1.x, p1.y), Point(p2.x, p1.y))
        # down
        down_l = Line(Point(p1.x, p2.y), Point(p2.x, p2.y))

        # draw line
        if self.has_left_wall:
            self._win.draw_line(left_l, fill_color)
        if self.has_right_wall:
            self._win.draw_line(right_l, fill_color)
        if self.has_top_wall:
            self._win.draw_line(top_l, fill_color)
        if self.has_down_wall:
            self._win.draw_line(down_l, fill_color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid),
                        Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid),
                        Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2),
                        Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid),
                        Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)

    def get_size(self):
        width = abs(self._x2 - self._x1)
        height = abs(self._y2-self._y1)
        return width, height
