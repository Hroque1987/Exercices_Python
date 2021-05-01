def func(**kwargs): # passing keyword parameters woth **
    print(kwargs)

func(a=1, b=42) # pass two keyword parameters
func(**{'a': 1, 'b': 42}) # unpack
func(**dict(a=1, b=42)) # unpack
