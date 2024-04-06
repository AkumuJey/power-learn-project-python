class Vehicle:
    def parent(self):
        print("Mimi ni mzae")

class Car(Vehicle):
    def __init__(self, make, year):
        self.__make = make
        self.__year = year

    def getDetails(self):
        print(f"{self.__make} was made in {self.__year}")

gari1 = Car("Toyota", 1977)
gari1.getDetails()
gari1.parent()