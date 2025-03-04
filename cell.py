from window import Window
from geometry import Point, Line
class Cell():
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window = None, 
                 has_left_wall = True,
                 has_right_wall = True,
                 has_top_wall = True,
                 has_bottom_wall = True):
        self._x1 = min(x1, x2)
        self._x2 = max(x1, x2)
        self._y1 = min(y1, y2)
        self._y2 = max(y1, y2)
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall
        self.visited = False
    
    def draw(self) -> None:
        left_color = "black" if self.has_left_wall else "white"
        right_color = "black" if self.has_right_wall else "white"
        top_color = "black" if self.has_top_wall else "white"
        bottom_color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(line=Line(Point(self._x1, self._y1), 
                                Point(self._x1, self._y2)),
                        fill_color=left_color)
        self._win.draw_line(line=Line(Point(self._x2, self._y1), 
                                Point(self._x2, self._y2)),
                        fill_color=right_color)
        self._win.draw_line(line=Line(Point(self._x1, self._y1), 
                                Point(self._x2, self._y1)),
                        fill_color=top_color)
        self._win.draw_line(line=Line(Point(self._x1, self._y2), 
                                Point(self._x2, self._y2)),
                        fill_color=bottom_color)
    
    def get_center(self) -> Point:
        return Point( (self._x1 + self._x2)/2, (self._y1 + self._y2)/2 ) 

    def draw_move(self, to_cell, undo = False) -> None:
        center_1 = self.get_center()
        center_2 = to_cell.get_center()
        color = "gray" if undo else "red"
        self._win.draw_line(line=Line(center_1, center_2), fill_color=color) 
        