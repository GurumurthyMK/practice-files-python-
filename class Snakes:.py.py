class Snakes:
    def __init__(self, name, venomous, bites):
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
    pass
# Create instances
cobra = Cobra("cobra", "is venomous", "bites aggressively")
green_snake = GreenSnakes("green snake", "is mildly venomous", "rarely bites")
rat_snake = RatSnakes("rat snake", "is not venomous", "bites if provoked")

# Call methods on instances
cobra.show_bites()
cobra.show_venomous()
green_snake.show_bites()
green_snake.show_venomous()
rat_snake.show_bites()
rat_snake.show_venomous()