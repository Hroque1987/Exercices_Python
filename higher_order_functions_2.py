# Higher Order Function = a funcation that either:
#                           1. accepts a function as argument
#                                   or
#                           2. returns a function
#                           (in python, functions are also treated as objects)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend # 1-returns the function dividend

divide = divisor(2) # 2- assigns 2 to x and returns fucntio
                    #   dividend and assgigns that function to variable divide


print(divide(10)) # 3- divide now as the function dividend stored so we can assign 10 to y



