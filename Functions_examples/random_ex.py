import random

x = random.randint(1,6)
Y = random.random()

mylist = ['rock', 'paper', 'scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,'j','q','k','a']
random.shuffle(cards)
print(cards)

print(z)



