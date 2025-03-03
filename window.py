from tkinter import Tk, BOTH, Canvas
from geometry import Line

class Window():
    def __init__(self, width, height, title="This is title"):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = title
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.widget = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.widget.pack()
        self.running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_color: str):
        line.draw(canvas=self.widget, fill_color=fill_color)
        