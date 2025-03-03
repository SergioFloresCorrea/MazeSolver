from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas: Canvas, fill_color):
        x1, y1 = self.point_1.x, self.point_1.y
        x2, y2 = self.point_2.x, self.point_2.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
        
