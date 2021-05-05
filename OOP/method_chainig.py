# method chaining is used to call multiple methods sequencialy

class Car:

    def turn_on(self):
        print('You started the engine!')
        return self
    
    def drive(self):
        print('You drive the car')
        return self
    
    def brake(self):
        print('You step on the brake!')
        return self
    
    def turn_off(self):
        print('You turn off the engine!')
        return self
car = Car()

car.drive()
car.brake()

car.drive().brake()

car.turn_on().drive().brake().turn_on()


