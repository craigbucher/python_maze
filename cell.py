from graphics import Line, Point

# Let's build a Cell class that holds all the data about an individual cell. 
# It should know which walls it has, know where it exists on the canvas in x/y
# coordinates, and have access to the window so that it can draw itself:

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False     
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    # The Cell class needs to be able to draw itself to its canvas. 
    # It should take the x/y coordinates of its top-left corner, and its 
    # bottom-right corner as input:
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # If the cell has a left wall, draw it:
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        # If the cell has a top wall, draw it:
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        # If the cell has a right wall, draw it:
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        # If the cell has a bottom wall, draw it:
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    # We need a way to draw a path between 2 cells. It should draw a 
    # line from the center of one cell to another
    def draw_move(self, to_cell, undo=False):
        # Calculate center coordinates of current cell:
        x_center = (self._x1 + self._x2) // 2
        y_center = (self._y1 + self._y2) // 2
        
        x_center2 = (to_cell._x1 + to_cell._x2) // 2
        y_center2 = (to_cell._y1 + to_cell._y2) // 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
