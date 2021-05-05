class Animal:

    def eat(self):
        print('This animal eats!')

class Rabbit(Animal):
    
    def eat(self): #overrriding the animal method
        print('This rabbit eats!')



rabbit = Rabbit()
rabbit.eat()
