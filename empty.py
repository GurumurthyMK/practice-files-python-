class Snakes:
    def __init__(self,name,venomous,bites):
        self.name = name
        self.venomous = venomous
        self.bites = bites

    def show_bites(self):
        print(f"the {self.name} {self.bites}")
    def show_venomous(self):
        print(f"the {self.name} {self.venomous}")

class Cobra(Snakes):
    pass
class GreenSnakes(Snakes):
    pass
class RatSnakes(Snakes):
    def show_bites(self):
        print(f"the rat snake does bite but is harmless")
    def show_venomous(self):
        print("the rat snake is not venomous")
Cobra = Cobra()
GreenSnakes = GreenSnakes()
RatSnakes = RatSnakes()


Cobra.show_bites()
Cobra.show_venomous()
GreenSnakes.show_bites()
GreenSnakes.show_venomous()
RatSnakes.show_bites()
RatSnakes.show_venomous()
