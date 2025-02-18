""" 
#! -----Note----- 

* __init__():
1. Dunder method
2. Constructor
3. No return

* 3 type of constructor:
1. default constructor.
2. Parameterized constructor.
3. Default value constructor.

* Every function in the class are called "method".

"""

class Car:
    def __init__(self):
        print("Hi. i'm default constructor.")
        self.brand = ""
        self.model = ""

    def __init__(self, brand, model):
        print("Hi. i'm Parameterized constructor.")
        self.brand = brand
        self.model = model

    def __init__(self, brand="BMW", model="X9"):
        print("Hi. i'm Default value constructor.")
        self.brand = brand
        self.model = model


car1 = Car()
car1.brand = "Toyota"
print(car1.brand)

car2 = Car("Tesla", "M3")
print(car2)

car3 = Car()
print(car3)
