from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.speed('fastest')

        self.refresh()

    def refresh(self):
        self.screen = Screen()
        x = random.randint(-int(self.screen.window_width() / 2 - 20), int(self.screen.window_width() / 2 - 20))
        y = random.randint(-int(self.screen.window_height() / 2 - 20), int(self.screen.window_height() / 2 - 20))
        self.goto(x, y)
