#Duck typing = concept where the class of an object is less important than the methods 
#               class type is not checked if the minimum/attributes are present
#               'if it walks like a duck, and it quacks like a duck, then it must be a duck'

class Duck:

    def walk(self):
        print('This duck is walking')

    def talk(self):
        print('This duck is quaking')


class Chicken:

    def walk(self):
        print('This chicken is walking')

    def talk(self):
        print('This chicken is clucking')

class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('you cought the critter')

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken) # you can pass a chicken object as long it has the same methods