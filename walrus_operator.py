# walrus operator :=

# new to python 3.8
#assignment expression aka walrus operator
#assigns values to variables as part of a larger expression

#happy = True

#print(happy)

#print(happr = True) cant do that

print(happy := True)
print(happy)


foods = list()

while True:
    food = input('Wat food do you like? :')
    if food == 'quit':
        break
    foods.append(food)

# or you can write this code with
foods = list()

while food := input('Wat food do you like?:') != 'quit':
    foods.append(food)


    

