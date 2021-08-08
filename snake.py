from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_square(i)

    def add_square(self, i):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(i)
        self.squares.append(new_square)

    def extend(self):
        self.add_square(self.squares[-1].position())

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def move(self):
        # right boundaries
        if self.head.xcor() > 300:
            self.head.goto(-290, self.head.ycor())

        # left boundaries
        if self.head.xcor() < -300:
            self.head.goto(290, self.head.ycor())

        # upper boundaries
        if self.head.ycor() > 300:
            self.head.goto(self.head.xcor(), -290)

        # bottom boundaries
        if self.head.ycor() < -300:
            self.head.goto(self.head.xcor(), 290)

        for i in range(len(self.squares) - 1, 0, -1):
            # print(i)
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
