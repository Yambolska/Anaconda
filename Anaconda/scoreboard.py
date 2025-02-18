from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,):
        super().__init__()
        self.pen()
        self.teleport(x=-20,y=270)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(arg=f'Score:{self.score}',align='center',font=('Arial', 20, 'normal'))

    def gameover(self):
        self.home()
        self.write(arg=f'GAME OVER',align='center',font=('Arial', 20, 'normal'))

    def increase(self):
        self.clear()
        self.score+=1
        self.write(arg=f'Score:{self.score}', align='center', font=('Arial', 20, 'normal'))









