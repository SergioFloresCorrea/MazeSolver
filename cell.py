from window import Window
from geometry import Point, Line
class Cell():
    def __init__(self, x1: int, y1: int, x2: int, y2: int, win: Window, 
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
    
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(line=Line(Point(self._x1, self._y1), 
                                    Point(self._x1, self._y2)),
                          fill_color="black")
        if self.has_right_wall:
            self._win.draw_line(line=Line(Point(self._x2, self._y1), 
                                    Point(self._x2, self._y2)),
                          fill_color="black")
        
        if self.has_top_wall:
            self._win.draw_line(line=Line(Point(self._x1, self._y1), 
                                    Point(self._x2, self._y1)),
                          fill_color="black")
        
        if self.has_bottom_wall:
            self._win.draw_line(line=Line(Point(self._x1, self._y2), 
                                    Point(self._x2, self._y2)),
                          fill_color="black")