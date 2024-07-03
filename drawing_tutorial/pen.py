from turtle import Turtle, Screen
# 建立畫布
screen = Screen()

# 建立畫筆
turtle = Turtle()

# 移動方向
# turtle.penup() # 不會在圖上留下痕跡
turtle.goto(-50, 100)
# turtle.pendown() # 會在圖上留下痕跡
turtle.goto(200, 100)

# 保持畫布開啟
screen.mainloop()