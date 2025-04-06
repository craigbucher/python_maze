from tkinter import Tk, BOTH, Canvas
# See tkinter documentation for explanation of __init__ commands

class Window:
    # The constructor should take a width and height:
    def __init__(self, width, height):
        # It should create a new root widget using Tk() and save it as a data member:
        self.__root = Tk()
        # Set the title property of the root widget:
        self.__root.title("Maze Solver")
        # Create a Canvas widget and save it as a data member:
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        # Pack the canvas widget so that it's ready to be drawn:
        self.__canvas.pack(fill=BOTH, expand=1)
        # Create a data member to represent that the window is "running", and set it to False:
        self.__running = False
        # You'll also need to add another line to the constructor to call the 
	   # protocol method on the root widget, to connect your close method to 
	   # the "delete window" action. This will stop your program from running 
	   # when you close the graphical window:
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # The redraw() method on the window class should simply call the root 
    # widget's update_idletasks() and update() methods. Each time this is 
    # called, the window will redraw itself:
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # This method should set the data member we created to track the "running"
    # state of the window to True. Next, it should call self.redraw() over 
    # and over as long as the running state remains True
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    # We need a draw_line method on our Window class. It should take an 
    # instance of a Line and a fill_color as inputs, then call the Line's 
    # draw() method.
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # the close() method should simply set the running state to False:
    def close(self):
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x	# x=0 is the left of the screen.
        self.y = y	# y=0 is the top of the screen.

# The line class has a bit more logic in it. Its constructor should take 
# 2 points as input, and save them as data members:
class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    # The Line class needs a draw() method that takes a Canvas and a "fill 
    # color" as input. The fill_color will just be a string like "black" or "red":
    def draw(self, canvas, fill_color="black"):
        # Next it should call the Canvas's create_line method:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

