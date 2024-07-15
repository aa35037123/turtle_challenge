from turtle import Turtle, Screen
# 建立畫布
screen = Screen()

# 建立畫筆
pen = Turtle()

# 移動方向
pen.penup() # 不會在圖上留下痕跡
pen.goto(-50, 100)
pen.pendown() # 會在圖上留下痕跡
pen.goto(200, 100)

# 保持畫布開啟
screen.mainloop()