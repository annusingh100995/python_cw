class Shape():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self,x,y,r):
        Shape.__init__(self,x,y)
        self.r = r

    def __str__(self):
        return "Circle (x,y,r):({},{},{})".format(self.x,self.y,self.r)

class Rectangle(Shape):
    def __init__(self,x,y,height,width):
        Shape.__init__(self,x,y)
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width

    def __str__(self):
        return "Rectangle (x,y,height,width): ({},{},{},{})".format(self.x,self.y,self.height,self.width)

class Square(Rectangle):
    def __init__(self,x,y,side):
        Rectangle.__init__(self,x,y,side,side)

    def __str__(self):
        return "Square (x,y,side):({},{},{})".format(self.x,self.y,self.height)

print(Circle(1,2,3))
print( Square(4,5,6) )
print( Rectangle(1,2,3,4) )
print( Rectangle(1,2,3,4).area() )
print( Square(4,5,6).area())
print( Square(4,5,6).area())
