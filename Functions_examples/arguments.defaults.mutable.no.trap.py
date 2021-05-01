def func(a= None):
    if a is None:
        a= []

    '''Note that, by using the preceding technique, if a isn't passed when calling the
    function, you always get a brand new empty list.'''
