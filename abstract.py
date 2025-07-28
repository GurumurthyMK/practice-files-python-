from abc import ABC, abstractmethod

class Staff(ABC):

    @abstractmethod
    def beats(self):
        pass
    @abstractmethod
    def kills(self):
        pass

class Principal(Staff):
    def beats(self):
        print("the principal beats kids too much")
    def kills(self):
        print("the principal kills children secretly")
class good_teacher(Staff):
    def beats(self):
        print("the good teach stops the pinci from beating")
    def kills(self):
        print("she was the one who killed the monstrous princi 😗!")

princi = Principal()
angel = good_teacher()
princi.beats()
princi.kills()
angel.beats()
angel.kills()
