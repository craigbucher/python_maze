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
		
		self._create_cells()
		
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
		
		
