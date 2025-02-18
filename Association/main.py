class Laptop:
    def __init__(self, brand="None"):
        self.brand = brand

class Student:
    def __init__(self, name, Laptop_obj):
        self.name = name
        self.laptop_V = Laptop_obj

    def show(self):
        print(f"{self.name} has a laptop named {self.laptop_V.brand}")

l1 = Laptop("Mac")
s1 = Student("shiam", l1)
s1.show()
