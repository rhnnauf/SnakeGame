from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)

        self.update_score()

        # self.add_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        hs = int(self.read_hs())
        self.write(f'Score : {self.score} High Score : {hs}', align='center', font=('Arial', 20, 'normal'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.overwrite_hs(self.highscore)

        self.score = 0
        self.update_score()

    def overwrite_hs(self, highscore):
        hs = str(highscore)
        with open('high_score.txt', mode='w') as file:
            file.write(hs)

    def read_hs(self):
        with open('high_score.txt') as file:
            highscore = file.read()
            return highscore