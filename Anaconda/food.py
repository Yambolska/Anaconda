from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.replace()



    def replace(self):
        x=random.randint(0,280)
        y=random.randint(0,280)
        self.teleport(x=x,y=y)
