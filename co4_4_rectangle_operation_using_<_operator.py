class Rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()


l1 = int(input("Enter the length of Rectangle 1: "))
w1 = int(input("Enter the width of Rectangle 1: "))
r1 = Rectangle(l1, w1)

l2 = int(input("Enter the length of Rectangle 2: "))
w2 = int(input("Enter the width of Rectangle 2: "))
r2 = Rectangle(l2, w2)

if r1 < r2:
    print(f"Area of Rectangle 2 is greater: {r2.area()}")
else:
    print(f"Area of Rectangle 1 is greater: {r1.area()}")
