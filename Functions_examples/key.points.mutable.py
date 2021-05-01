x= list(range(3))

def func(x):
    x[1] = 42 # this affectes the caller.

func(x)
print(x)
