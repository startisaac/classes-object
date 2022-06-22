class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.tracks = tracks

    def get_score(self, score=30.50):
        self.score = score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("isaac")
Bob.change_age(30)
Bob.add_track("Fullstack")
Bob.get_score()


print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)