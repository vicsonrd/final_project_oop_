from turtle import *
from math import *
from abc import ABC, abstractmethod

# Base abstract class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Sunflower class
class Sunflower(Shape):
    def __init__(self, petals=16, seeds=140):
        self.petals = petals
        self.seeds = seeds

    def draw(self):
        speed(0)
        bgcolor("black")
        goto(0, -40)

        # Draw petals
        for i in range(self.petals):
            for j in range(18):
                color('#FFA216'), rt(90)
                circle(150 - j * 6, 90), lt(90)
                circle(150 - j * 6, 90), rt(180)
            circle(40, 24)

        # Draw seeds in center
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


# Small heart in the middle
class SmallHeart(Shape):
    def __init__(self, size=50, color_fill="pink"):
        self.size = size
        self.color_fill = color_fill

    def draw(self):
        penup()
        goto(0, 0)  # center of sunflower
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


# Main program
if __name__ == "__main__":
    sunflower = Sunflower()
    sunflower.draw()

    small_heart = SmallHeart(size=50, color_fill="pink")
    small_heart.draw()

    hideturtle()
    done()
