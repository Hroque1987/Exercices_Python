#filter() = creates a collection of elements from an iterable for witch a function returns true

#filter(function,iterable)

friends = [('Rachel',19),
           ('Monica',18),
           ('Phoebe',17),
           ('Joey',21),
           ('chandler',21),
           ('Ross',20)]

age = lambda data:data[1] >18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
    print(i)
