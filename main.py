class rectangle():
    def __init__(self, l , w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.legth*self.width

newRectangle = Rectangle(12, 10)
print("dimension of Rectangle - Length : %d width : %d" % (newRectangle.length, newRectangle.width))
print("Area of rectangle :", newRectangle.rectangle_area())