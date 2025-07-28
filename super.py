# using a super() class
class WildLife:
    def __init__(self, name, living, predator, prey):
        self.name = name 
        self.living = living
        self.predator = predator
        self.prey = prey

    def describe(self):
        print(f"The {self.name} is a natural {self.predator} and is {self.living}")

class aquatic_mams(WildLife):
    def __init__(self, name, living, predator, prey, livesin):
        super().__init__(name, living, predator, prey)
        self.livesin = livesin

    def describe(self):
        super().describe()
        print(f"It lives in {self.livesin}.")

# Example usage:
dolphin = aquatic_mams("Dolphin", "alive", "predator", "fish", "ocean")
dolphin.describe()