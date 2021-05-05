from car import Car

car_1 = Car('Chevy', 'Corvette', 2020, 'blue')
car_2 = Car('ford', 'escort', 1994, 'red')


#print(car_1.model)
#print(car_1.make)
#print(car_1.year)
#print(car_1.color)

car_1.drive()
car_1.stop()


car_1.wheels = 2 # changing the default only for car 1
print(car_1.wheels)
print(car_2.wheels) # car 2 remais with default

print(Car.wheels) 
Car.wheels = 2 # change the default wheels for all instances of class
print(Car.wheels) 