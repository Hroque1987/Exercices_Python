age = list(range(20,25))
name = ['Jonh', 'Maria', 'Ze', 'Peter', 'Chloe']
name_age = list(zip(name,age))
print(name_age)
drink_age =list(filter(lambda person: person[1] > 21 ,name_age))
print(drink_age)
