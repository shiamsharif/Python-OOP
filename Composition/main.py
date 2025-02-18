class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, power):
        self.brand =  brand
        self.engine = Engine(power)

    def show(self):
        print(f"{self.brand} has an engine with {self.engine.power}")


c1 = Car("BMW", 750)
c1.show()