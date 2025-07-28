# the main class(top)
class cats:
    def __init__(self,name):
       self.name = name
    def speaks(self):
        print("Meowwww!!!")
    def agility(self):
        print(f"{self.name} are highly agile")

# the 1st level subclass inhereting main class
class cat_breeds(cats):
   def cost(self):
      print("british cats are highly costly")

#2nd level subclass inhereting level 1 class
class sub_breed1(cat_breeds):
   def color(self):
      print(f"{self.name} are gold in color ")

#3rd level of subclass inhereting both 2nd level and 1st level
class sub_breed2(sub_breed1,cat_breeds):
   def shape(self):
      print(f"{self.name} are short haired cats")
   

Cat_breeds = cat_breeds("British Cats")
Sub_breed1 = sub_breed1("Golden Maincounes")
Sub_breed2 = sub_breed2("British short hair")

Cat_breeds.cost()
Cat_breeds.speaks()