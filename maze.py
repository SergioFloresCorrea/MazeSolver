import time
import random
from window import Window
from cell import Cell

class Maze():
    def __init__(self, x1: int, y1: int, 
                 num_rows: int, num_cols: int, 
                 cell_size_x: int, cell_size_y: int,
                 win: Window = None, seed: int =None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self.solve()
    
    def _create_cells(self):
        self._cells = [
                        [None for _ in range(self.num_rows)] 
                        for _ in range(self.num_cols)
                      ]
        
        for row, cells in enumerate(self._cells):
            for col, cell in enumerate(cells):
                self._draw_cell(row, col)
        

    def _draw_cell(self, i, j):
        if self._cells[i][j] is None:
            x1 = self._x1 + i * self._cell_size_x
            y1 = self._y1 + j * self._cell_size_y
            x2 = x1 + self._cell_size_x
            y2 = y1 + self._cell_size_y
            self._cells[i][j] = Cell(x1, y1, x2, y2, self._win)
        if self._win:
            self._cells[i][j].draw()
            self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        if self._win:
            self._draw_cell(0, 0)
            self._draw_cell(-1, -1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            indexes = [("bottom", i, j+1), ("top", i, j-1), ("left", i-1, j), ("right", i+1, j)]
            filtered_indexes = [
                    (direction, x, y) for direction, x, y in indexes 
                    if 0 <= x < self.num_cols and 0 <= y < self.num_rows
                ]
            adjacent_cells = [
                self._cells[a][b] for _, a, b in filtered_indexes if not self._cells[a][b].visited
                             ]
            if len(adjacent_cells) == 0:
                self._draw_cell(i, j)
                return 
            direction, a, b = random.choice(filtered_indexes)
            match direction:
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[a][b].has_bottom_wall = False
                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[a][b].has_top_wall = False
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[a][b].has_right_wall = False
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[a][b].has_left_wall = False
            self._break_walls_r(a, b)

    def _reset_cells_visited(self):
        for row, cells in enumerate(self._cells):
            for col, cell in enumerate(cells):
                self._cells[row][col].visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        indexes = [("bottom", i, j+1), ("top", i, j-1), ("left", i-1, j), ("right", i+1, j)]
        filtered_indexes = [
                    (direction, x, y) for direction, x, y in indexes 
                    if 0 <= x < self.num_cols and 0 <= y < self.num_rows
                    ]
        for direction, a, b in filtered_indexes:
            match direction:
                case "bottom":
                    if not self._cells[i][j].has_bottom_wall and not self._cells[a][b].visited:
                        self._cells[i][j].draw_move(self._cells[a][b])
                        truth_value = self._solve_r(a, b)
                        if truth_value:
                            return True
                        self._cells[i][j].draw_move(self._cells[a][b], undo=True)
                case "top":
                    if not self._cells[i][j].has_top_wall and not self._cells[a][b].visited:
                        self._cells[i][j].draw_move(self._cells[a][b])
                        truth_value = self._solve_r(a, b)
                        if truth_value:
                            return True
                        self._cells[i][j].draw_move(self._cells[a][b], undo=True)
                case "left":
                    if not self._cells[i][j].has_left_wall and not self._cells[a][b].visited:
                        self._cells[i][j].draw_move(self._cells[a][b])
                        truth_value = self._solve_r(a, b)
                        if truth_value:
                            return True
                        self._cells[i][j].draw_move(self._cells[a][b], undo=True)
                case "right":
                    if not self._cells[i][j].has_right_wall and not self._cells[a][b].visited:
                        self._cells[i][j].draw_move(self._cells[a][b])
                        truth_value = self._solve_r(a, b)
                        if truth_value:
                            return True
                        self._cells[i][j].draw_move(self._cells[a][b], undo=True)
        
        return False