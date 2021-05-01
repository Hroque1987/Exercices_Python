def minimum(*n):
    print(n) # n is a tuple
    if n:
        minimum_n =n[0]
        for value in n[1:]:
            if value < minimum_n:
                minimum_n = value
        print(minimum_n)

minimum(1,4,6,3,4,5,6,77,33,2,1)

# by using * in te function minimum we can pass a variable number of positional arguments.
