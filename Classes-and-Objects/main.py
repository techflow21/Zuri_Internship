class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score

    def change_name(self, name):
        return self.change_name
        
    def change_age(self, age):
        print('My age is ', Bob.age)
    
    def add_track(self, track):
        print('My tracks are ', Bob.tracks)

    def get_score(self):
        print("My score is ", Bob.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
 