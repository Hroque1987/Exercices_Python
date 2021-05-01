x = list(range(3))

def func(x):
    x[2] = 34 # changes the calller
    x = 'something else' #  points x to a new string inside local scope

func(x)
print(x)
