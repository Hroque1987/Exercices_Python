#str.format()


#animal ='cow'
#item = 'moon'

#print('The '+animal+' jumped over '+item)

#print('The {} jumped over the {}'.format(animal, item))

#print('The {1} jumped over the {0}'.format(animal, item)) #positional argument

#print('The {animal} jumped over the {item}'.format(animal='cow', item='moon')) # keyword argument

#text = 'The {} jumped over {}'
#print(text.format(animal,item))

#name ='Helder'

#print('Hello, my name is {}'.format(name))
#print('Hello, my name is {:10} nice to meet you'.format(name)) # add padding to a value
#print('Hello, my name is {:<10}nice to meet you'.format(name))
#print('Hello, my name is {:>10}nice to meet you'.format(name))
#print('Hello, my name is {:^10}nice to meet you'.format(name))

#number = 3.14159

#print('The number pi is {:.3f}'.format(number))

number =1000
print('The number is {:,}'.format(number))
print('The number is {:b}'.format(number))
print('The number is {:o}'.format(number))
print('The number is {:x}'.format(number))
print('The number is {:e}'.format(number))
