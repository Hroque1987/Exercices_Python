def func(*args):
    print(args)

values = (1,4,5,3)
func(values)  # equivalent to: func((1, 3, -7, 9)) we call func with one argument, a four elements tuple

func(*values)  # equivalent to: func(1, 3, -7, 9)
               # unpacking, which means that the four elements tuple is unpacked,
               # and the function is called with four arguments: 1, 3, -7, 9.
