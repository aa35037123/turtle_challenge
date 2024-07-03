from turtle import Turtle, Screen
# 建立畫布
screen = Screen()

# 建立畫筆
turtle = Turtle()
# 填充顏色
screen.colormode(255)

turtle.fillcolor((0, 255, 0))
# turtle.begin_fill()
for _ in range(5):
    turtle.forward(100)
    turtle.left(144)
# turtle.end_fill()

# 保持畫布開啟
screen.mainloop()