def func(a, b=4, c=88): # sets b and c to have standard values
    print(a, b, c)

func(1) # sets a to be 1 positional argument
func(b=45, c=12, a=78) # keyword arguments
func(42, c=9) # sets a to 42, anc c to 9, positional arguments must be on the left
func(23, 45, c=34)
#func(b=1, c=2, 42) example of error should be: func(42,b=1, c=2,)
