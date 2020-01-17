# 52 type of variables in class(class variables & instance variables)
class Car:
    def __init__(self):
        self.mod = 10
        self.camp = 'bmw'

c1 = Car()
c2 = Car()

c1.mod = 8
Car.wheel = 4
print(c1.mod,c1.camp,c1.wheel)
print()

print(c2.mod)
print(c2.camp)
