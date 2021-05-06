# map() = applies a funtion to each item in a iterable (list, tuple, etc)
#
# map(function,iterable)

store= [('shirt', 20.00),
        ('pants', 25.00),
        ('jacket', 50.00),
        ('socks', 10.00)]

# convert to euros 0.82

conversion_rate = 0.82

to_euros = lambda data: (data[0],data[1]*conversion_rate)
to_dollars = lambda data: (data[0],data[1]/conversion_rate)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)


