


class Point:
    def __str__(self):
        return "A dull class"


print(Point())

p = Point()
print(p.__str__())


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(x,y):({},{})".format(self.x, self.y)

    def area(self):
        return self.side * self.side


print(Point(1,2))

class Square:
    def __init__(self,x,y,side):
        self.x = x
        self.y = y
        self.side = side
        # self.p = p
        # self.q = q

    def area(self):
        return self.side*self.side

    def __str__(self):
        return "Square (x,y,side):({},{},{})".format(self.x, self.y, self.side)

    def location(self, p, q):
        dist = ((self.x-p)*(self.x-p))+((self.y-q)*(self.y-q))
        if dist < (self.side*self.side):
            return "The point ({},{}) is INSIDE the square".format(p,q)
        else:
            return  "The point ({},{}) is OUTSIDE the square".format(p,q)


#s = Square(1,2,5,2,5) # a square
#s = Square(1,2,5,3,5) # a square

s = Square(1,2,5) # a sqaure
print(s)
print(s.area())
print(s.location(2,5)) # false
print(s.location(2,0)) # true

t = Square(1,5,6)
print(t)
print(t.area())
# print(t.location(22,52))

t2 = Square(1,5,6)
print(t2)
print(t2.area())
# print(t2.location(2,3))

class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return self.r*self.r*3.14

    def __str__(self):
        return "Circle (x,y,r):({},{},{})".format(self.x, self.y, self.r)

    def location(self,p,q):
        dist = 0
        dist =  ((self.x-p)*(self.x-p))+((self.y-q)*(self.y-q))
        if dist <= (self.r*self.r):
            return "The point ({},{}) is INSIDE the circle".format(p,q)
        else:
            return  "The point ({},{}) is OUTSIDE the circle".format(p,q)


print("The circle data")
c1 = Circle(0,0,5)
print(c1.area())
print(c1.location(1,3))

c1 = Circle(0,0,6)
print(c1.area())
print(c1.location(13,3))

c2 = Circle(0,0,7)
print(c2.area())
print(c2.location(7,8))

c3 = Circle(0,0,10)
print(c3.area())
print(c3.location(10,10))

c4 = Circle(0,0,7)
print(c4.area())
print(c4.location(2,4))
