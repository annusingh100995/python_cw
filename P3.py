class Curve():
    def __init__(self, *inputs):
        self.items = []
        for i in inputs:
            self.append_if_valid(i)

    def append_if_valid(self,item):
        if not isinstance(item,Point):
            raise TypeError("Curve only takes point")
        self.items.append(item)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.items[index]
        else:
            return Curve(*self.items[index])

    def __setitem__(self, index, item):
        if not isinstance(item,Point):
            raise TypeError("Curve only take points")
        self.items[index] = item

    def __str__(self):
        return "Curve:{}".format(self.items)

    def __repr__(self):
        s = ", "
        s = s.join([repr(x) for x in self.items])
        return "Curve({})".format(s)



class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Points: ( {}, {} )".format(self.x, self.y)

    def __repr__(self):
        return "Point({},{})".format(self.x,self.y)

#print(Curve(1,23,34,3,345,54))

#c = Curve(1,23,45,34,3,345,54)

#print(c[2])
#print(c[0:4])
#c[6] = 10
#print(c)
print("THE NEW SHIT")

d = Curve(Point(1,2),Point(5,6))
print(d)

