from turtle import *

class Face:

    def__init__(self, xpos, ypos):
    self.size = 90
    self.coord = (xpos, ypos)
    self.noseSize = 'small'

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawOutLine()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)

        def goHome(self):
            penup()
            goto(self.coord)

            setheading(0)

        def drawOutline(self):
            penup()

            forward(self.size)
            left(90)

            pendown()
            circle(self.size)

            self.goHome()

        def drawEye(self, turn):
            penup()

            left(turn)

            forward(self.size / 2)
            pendown()