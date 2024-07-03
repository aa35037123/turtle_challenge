import turtle
import sys

def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_square(t, size, color):
    draw_rectangle(t, size, size, color)

def draw_enderman(t):
    t.penup()
    t.goto(-50, 50)  # Move to start position
    t.pendown()

    # Draw the body
    draw_rectangle(t, 40, 100, 'black')
    
    # Draw the legs
    leg_positions = [(-50, -50), (-10, -50)]
    for pos in leg_positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_rectangle(t, 10, 70, 'black')
    
    # Draw the arms
    arm_positions = [(-70, 50), (30, 50)]
    for pos in arm_positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_rectangle(t, 10, 100, 'black')
    
    # Draw the head
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    draw_square(t, 40, 'black')
    
    # Draw the eyes
    eye_positions = [(-35, 130), (-15, 130)]
    for pos in eye_positions:
        t.penup()
        t.goto(pos)
        t.pendown()
        draw_square(t, 10, 'purple')

def drawing(t):
    t.speed(0)
    draw_enderman(t)

if __name__ == '__main__':
    result_path = sys.argv[1]  
    s = turtle.getscreen()
    t = turtle.Turtle()
    drawing()
    canvas = s.getcanvas()
    canvas.postscript(file=result_path)
    # s.mainloop()  # Keeps the turtle graphics window open
