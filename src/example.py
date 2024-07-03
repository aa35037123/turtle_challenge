from turtle import Turtle, Screen
# 建立畫布
screen = Screen()
screen.colormode(255)
screen.bgcolor(0, 255, 0)
screen.title("我的畫布")
screen.setup(600, 600)
screen.clearscreen()

# 建立畫筆
turtle = Turtle()

# 移動方向
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()

for side in range(3, 11):
    angle = 360 / side
    for _ in range(side):
        turtle.forward(100)
        turtle.right(angle)
screen.resetscreen()

# 填充顏色
screen.colormode(255)
turtle.fillcolor(0, 255, 0)

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

turtle.begin_fill()
for _ in range(5):
    turtle.forward(100)
    turtle.left(144)
turtle.end_fill()
screen.resetscreen()

turtle.hideturtle()