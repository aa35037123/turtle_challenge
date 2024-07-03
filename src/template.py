import turtle as turtle
import sys

def drawing(pen):
    ## TODO: Implement the drawing function
    return
"""
#################
!!Don't touch the code below!!
Unless you want to uncomment the 'turtle.done()' line
#################
'turtle.done()' is used to keep the turtle graphics window open
Uncomment the line if you want to see the turtle graphics window

However, when judging your code, we don't want to see the turtle graphics window, 
so we commented it
#################
"""
if __name__ == '__main__':
    result_path = 'result.ps'
    s = turtle.getscreen()
    pen = turtle.Turtle()
    
    
    drawing(pen)
    

    canvas = s.getcanvas()
    canvas.postscript(file=result_path)
    turtle.done() # Uncomment this line if you want to keep the turtle graphics window open
