# 도형 만들기

class Point:
    def __init__(self, x, y):
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError('x, y값은 정수만 가능합니다.')
        
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        if not (isinstance(p1, Point) and isinstance(p2, Point)):
            raise ValueError('p1, p2값은 Point 인스턴스만 가능합니다.')

        self.p1 = p1
        self.p2 = p2

    def get_area(self):
        dx, dy = self.get_dx_dy()
        return dx*dy
    
    def get_perimeter(self):
        dx, dy = self.get_dx_dy()
        return 2 * (dx + dy)

    def is_square(self):
        dx, dy = self.get_dx_dy()
        return dx == dy

    def get_dx_dy(self):
        return (abs(self.p1.x - self.p2.x), abs(self.p1.y - self.p2.y))

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())