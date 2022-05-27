class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str="Bob", age: int=26, tracks=["FE","BE"], score: float=20.90) -> None:
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score

    def change_name(self, string: str) -> None:
        self.name =string
        print(f"Name has changed to {self.name}")

    def change_age(self, number: int) -> None:
        self.age =number
        print(f"Age has changed to {self.age}")

    def add_track(self, string: str) -> None:
        self.tracks.append(string)
        print(f"Tracks now include {self.tracks}")

    def get_score(self) -> None:
        print(f"The score is {self.score}")
        
Bob = Student()

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
