class Engine:
    def __init__(self, hoarse_power):
        self.hoarse_power = hoarse_power

class Wheels:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size

class car:
    def __init__(self, name, model, hoarse_power, wheel_size):
        self.name = name
        self.model = model
        self.hoarse_power = Engine(hoarse_power)
        self.wheel_size = [Wheels(wheel_size) for _ in range(4)]
    
    def display(self):
        return (f"the car is {self.name}, model - {self.model} and of "
                f"{self.hoarse_power.hoarse_power}HP, with wheelsize of "
                f"{self.wheel_size[0].wheel_size} inches")
    

car1 = car("Ford", "Mustang", 700, 18)
print(car1.display())