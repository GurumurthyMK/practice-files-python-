class student:
    grad_year = 2027
    def __init__(self,name,grade,rank):
        self.name = name
        self.grade = grade
        self.rank = rank

    def info(self):
        print(f"student info: {self.name},{self.grade},{self.rank} ")