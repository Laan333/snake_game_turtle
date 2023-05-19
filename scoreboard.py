from turtle import Pen
ALLIGN = "center"
FONT =("Verdana",15, "normal")
class Scoreboard(Pen):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALLIGN,font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.penup()
        self.goto(0,0)

        self.write(f"GAME OVER", align=ALLIGN, font=FONT)