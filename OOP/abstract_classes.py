# prevents a uses from creating an object of that class
# + compels a user to overrride abstract methods in a child class

#abstract class = a class witch contains one or more abstract methods.
#abstract method = a method that has a declaration bur does not have an implementation
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print('You drive the car')

    def stop(self):
        print('STOP THE CAR')


class Motorcycle(Vehicle):

    def go(self):
        print('You ride the bike!')

    def stop(self):
        print('STOP THE BIKE')

#vehicle= Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
motorcycle.stop()




