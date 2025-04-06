from cell import Cell
import random
import time

# create a class that holds all the cells in the maze in a 2-dimensional 
# grid, a list of lists:
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        # initialize data members for all inputs, then call 
	   # its _create_cells() method:
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    # This method should fill a self._cells list with lists of cells. 
    # Each top-level list is a column of Cell objects. Once the matrix 
    # is populated it should call its _draw_cell() method on each Cell:
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    # This method should calculate the x/y position of the Cell based 
    # on i, j, the cell_size, and the x/y position of the Maze itself. 
    # The x/y position of the maze represents how many pixels from the
    # top and left the maze should start from the side of the window.
    # Once that's calculated, it should draw the cell and call the maze's 
    # _animate() method:
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    # The animate method is what allows us to visualize what the 
    # algorithms are doing in real time. It should simply call the 
    # window's redraw() method, then use time.sleep() for a short 
    # amount of time so your eyes keep up with each render frame. I 
    # slept for 0.05 seconds:
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    # Add a _break_entrance_and_exit() method that removes an outer wall 
    # from those cells, and calls _draw_cell() after each removal:
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        # Can't use exact reference because maze size is variable:
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    # We need to break down enough walls that the maze is fun and challenging while also ensuring that 
    # there is a correct path from the start to the end.
    # This recursive method is a depth-first traversal through the cells, breaking down walls as it goes:
    def _break_walls_r(self, i, j):
        # Mark the current cell as visited:
        self._cells[i][j].visited = True
        while True:
            # Create a new empty list to hold the i and j values you will need to visit:
            next_index_list = []

            # Check the cells that are directly adjacent to the current cell. 
            # Keep track of any that have not been visited as "possible directions" to move to
            
            # left:
            # 'if i > 0': This ensures that you're not trying to check a cell above the first row (i = 0).
            # 'and not self._cells[i - 1][j].visited': This checks whether the cell 
            # directly above the current cell (i - 1, j) has already been visited. 
            # If it has not been visited, it's a valid target for moving to and breaking walls
            if i > 0 and not self._cells[i - 1][j].visited:
                # next_index_list.append((i - 1, j)): If both conditions are true, 
                # the i and j coordinates of the cell above are added to the next_index_list. 
                # This list is keeping track of potential next cells to visit:
                next_index_list.append((i - 1, j))
            # right:
            # 'if i < self._num_cols - 1': This ensures that you don’t try to access a cell 
            # below the last column. 
            # 'and not self._cells[i + 1][j].visited': This checks whether the cell immediately 
            # below the current one (i + 1, j) has already been visited. If it's untouched 
            # (visited == False), then it's a valid candidate for the next step in your depth-first traversal.
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up:
            # 'if j > 0': This ensures that you don’t attempt to check a cell to the left 
            # of the first column (j = 0).
            # 'and not self._cells[i][j - 1].visited': This checks whether the cell immediately to 
            # the left of the current cell (i, j - 1) has already been visited. If it hasn’t been 
            # visited yet, it qualifies as a valid candidate for movement and wall-breaking:
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down:
            # 'if j < self._num_rows - 1': This checks if we're safely within the bounds of the
            # grid and not trying to step beyond the right edge.
            # 'and not self._cells[i][j + 1].visited': This ensures that the cell immediately to the 
            # right of the current one (i, j + 1) hasn’t already been visited:
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if next_index_list is empty, it indicates that all adjacent cells are either out 
            # of bounds or have already been visited.
            if len(next_index_list) == 0:
            	 # call a method to "draw" or mark the current cell (i, j) in the maze:
                self._draw_cell(i, j)
                # exit the recursion completely for this particular function call, signaling 
                # that the traversal cannot go any further in this direction:
                return

            # randomly choose the next direction to go:
            # By selecting a random direction from the list of possible moves, the maze 
            # generation becomes unpredictable, leading to unique maze paths every time the 
            # algorithm runs (unless you seed it, of course)
            # Generate a random number between 0 and len(next_index_list) - 1. In other words, 
            # it chooses a random index from the list of possible next directions (stored in next_index_list).
            direction_index = random.randrange(len(next_index_list))
            # With the randomly chosen index, this selects the corresponding (i, j) coordinates 
            # from next_index_list. These coordinates represent the next cell you'll visit 
            # (and likely break walls with):
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right:
            # 'next_index[0] == i + 1' means you're moving to the cell to the right of your current position:
            if next_index[0] == i + 1:
            	 # Remove: the right wall of the current cell:
                self._cells[i][j].has_right_wall = False
                # Remove the left wall of the cell to the right
                # (When you break a wall between two cells, you need to update both cells' 
                # wall information.)
                self._cells[i + 1][j].has_left_wall = False
            # left:
            # 'next_index[0] == i - 1' means you're moving to the cell to the left of your current position:
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down:
            # # 'next_index[0] == j + 1' means you're moving to the cell below your current position:
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up:
            # 'next_index[0] == j - 1' means you're moving to the cell above your current position:
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell:
            # After you've:
            #		Chosen a random unvisited neighbor cell (stored in next_index)	
            #		Broken down the walls between your current cell and that neighbor
            # Recursively call _break_walls_r() with the coordinates of that neighbor cell 
            # (next_index[0] and next_index[1]). This will continue the wall-breaking process 
            # from that new position.
            # (This recursive approach is key to the depth-first search algorithm for maze 
            # generation. It will continue exploring as deep as possible along each branch 
            # before backtracking)
            self._break_walls_r(next_index[0], next_index[1])
    
    # Write a _reset_cells_visited method to reset the 'visited' property of all the cells 
    # in the Maze to *False*. Call it after _break_walls_r so we can reuse the visited 
    # property when solving the maze in the next step:
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    # returns True if this is the end cell, OR if it leads to the end cell.
    # returns False if this is a loser cell.
    def _solve_r(self, i, j):
        # Call the _animate method:
        self._animate()
        # Mark the current cell as visited:
        self._cells[i][j].visited = True

        # If t the "end" cell (the goal) then return True:
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited:
        if (
            # make sure moving left won't go out of bounds:
            i > 0
            # ensure there's no wall blocking the path:
            and not self._cells[i][j].has_left_wall
            # make sure we haven't already visited the cell:
            and not self._cells[i - 1][j].visited
        ):
            # Draw a move from current cell to left cell:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            # Recursively call _solve_r on the left cell:
            if self._solve_r(i - 1, j):
                # If that recursive call returns True, return True 
                # (meaning a solution was found):
                return True
            # Otherwise, undo the move by drawing it again with 'undo=True' parameter 
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # If none of the directions worked out, return False:
        return False

    # Call maze.solve() in the main function to execute the depth-first search:
    # The solve() method on the Maze class simply calls the _solve_r method starting at 
    # i=0 and j=0. It should return True if the maze was solved, False otherwise. 
    # This is the same return value as _solve_r:
    def solve(self):
        return self._solve_r(0, 0)
