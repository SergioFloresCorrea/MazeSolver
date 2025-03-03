import geometry
from window import Window
from tkinter import Canvas
from cell import Cell

def main():
    win = Window(800, 600)
    point_1 = geometry.Point(0, 0)
    point_2 = geometry.Point(800, 600)
    cell_1 = Cell(80, 80, 120, 120, win) ## all sides
    cell_2 = Cell(120, 120, 160, 160, win, has_bottom_wall = False) # not bottom
    cell_3 = Cell(160, 160, 200, 200, win, has_top_wall = False) # not top
    cell_4 = Cell(200, 200, 240, 240, win, has_left_wall = False) # not left
    cell_5 = Cell(240, 240, 280, 280, win, has_right_wall = False) # not right
    cell_1.draw()
    cell_2.draw()
    cell_3.draw()
    cell_4.draw()
    cell_5.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()