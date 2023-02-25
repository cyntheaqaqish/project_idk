from inheritence.circle import Circle
from math import pi


class Ball(Circle):



    def volume(self):
        volume= (4/3)*pi*self.radius**3
        return volume
    def area(self):
        area = 4 *pi * self.radius

    def print_area(self):
        print("the area is " + str(super().area()))