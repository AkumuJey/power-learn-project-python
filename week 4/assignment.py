class Person:
    def __init__(self, name, age, gender) -> None:
        self.__name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"My name is {self.__name}, I am {self.age} years old and I am a {self.gender}.")


person1 = Person("Akumu J", 43, "male")
person1.introduce()
