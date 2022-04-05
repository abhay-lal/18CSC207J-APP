class Rectangle():
    l = 0
    b = 0

    def _init_(self, *s):
        if not len(s):
            self.l = 0
            self.b = 0
        elif len(s) == 1:
            self.l = self.b = s[0]
        else:
            self.l = s[0]
            self.b = s[1]

    def area(self):
        return self.l * self.b


obj1 = Rectangle(5)
print(obj1.area())
obj2 = Rectangle(2)
print(obj2.area())
obj3 = Rectangle(2, 4)
print(obj3.area())
