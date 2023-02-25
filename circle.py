#import math #we called a whole library of mathematical values
from math import pi 
class circle:
    def __init__(self, radius):
        self.radius = radius
    def circum(self):
        circum = self.radius*2* math.pi
        return circum #we use return to turn back to the function, instead of putting print (which the program will print the value all the time)
# the function without the return will only calculate the value and not print it
#and it helps if we want to compare values
    def area(self):
        area = self.radius**2* math.pi

#math.pi
c1 = circle(3)
print(c1.circum())

