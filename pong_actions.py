from turtle import Turtle, Screen

HW_LINE_LENGTH = 18
HW_LINE_WIDTH = 5
START_POSITIONS_R = [(480, 20), (480, 0), (480, -20)]
START_POSITIONS_L = [(-490, 20), (-490, 0), (-490, -20)]


class HalfwayLine():
    def __init__(self):
        halfway_line = Turtle()
        halfway_line.color("white")
        halfway_line.pencolor("white")
        halfway_line.penup()
        halfway_line.goto(0, 300)
        halfway_line.setheading(270)
        halfway_line.width(HW_LINE_WIDTH)

        for i in range(21):
            halfway_line.pendown()
            halfway_line.forward(HW_LINE_LENGTH)
            halfway_line.penup()
            halfway_line.forward(HW_LINE_LENGTH)


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=3)
        self.penup()
        self.goto(start_pos)

    def right_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def right_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)

    def left_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def left_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 20)


class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()


