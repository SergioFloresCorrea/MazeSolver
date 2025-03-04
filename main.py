import geometry
from window import Window
from tkinter import Canvas
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(40, 40, 8, 10, 40, 40, win, seed = 0)
    win.wait_for_close()

if __name__ == "__main__":
    main()