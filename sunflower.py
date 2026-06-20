from turtle import *
from math import *
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Sunflower(Shape):
    def __init__(self, petals=16, seeds=140):
        self.petals = petals
        self.seeds = seeds

    def draw(self):
        speed(0)
        bgcolor("black")
        goto(0, -40)

        for i in range(self.petals):
            for j in range(18):
                color('#FFA216'), rt(90)
                circle(150 - j * 6, 90), lt(90)
                circle(150 - j * 6, 90), rt(180)
            circle(40, 24)

        color('black')
        shape('circle')
        shapesize(0.5)
        fillcolor('#8B4513')
        golden_ang = 137.508
        phi = golden_ang * (pi / 180)

        for i in range(self.seeds):
            r = 4 * sqrt(i)
            theta = i * phi
            x = r * cos(theta)
            y = r * sin(theta)
            penup(), goto(x, y)
            setheading(i * golden_ang)
            pendown(), stamp()

class SmallHeart(Shape):
    def __init__(self, size=50, color_fill="pink"):
        self.size = size
        self.color_fill = color_fill

    def draw(self):
        penup()
        goto(0, 0)
        pendown()
        color(self.color_fill)
        begin_fill()
        left(50)
        forward(self.size)
        circle(self.size/2, 200)
        right(140)
        circle(self.size/2, 200)
        forward(self.size)
        end_fill()
        setheading(0)

if __name__ == "__main__":
    sunflower = Sunflower()
    sunflower.draw()

    heart = SmallHeart(size=50, color_fill="pink")
    heart.draw()

    # Add text after drawing
    penup()
    goto(0, -200)  # adjust position below the sunflower
    color("white")
    write("I love you Yana", align="center", font=("Comic Sans MS", 24, "bold"))

    hideturtle()
    done()
