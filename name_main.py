# if __name__ == '__main__'

# python interpreter setd ''special varialbles'', one of wich in __name__
# python will assign the __name__ variable a value of '__main__' if its the initial module being run


import map_function
print(__name__)

print(map_function.__name__)

if __name__ == '__main__':
    print('running this module directly')

else:
    print('running othes module indirectly')


