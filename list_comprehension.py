# list compreension = a way to create a new list with less sintax
#                     can mimic a lambda function, easier to read
#                     list = [expression, for item iterable]
#                     list = [expression for item iterable, if condition]
#                     list = [expression if/else for item iterable]
#


squares = []           # create an empty list
for i in range(1, 11): # create a for loop
    squares.append(i*i)# define what each loop iteration should do
print(squares)

# now with list compreension

squares1 = [i * i for i in range(1 ,11)]
print(squares1)

# mimic lambda functions

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students1 = [i for i in students if i >= 60]
print(passed_students1)

passed_students2 = [i if i >= 60 else 'Failed' for i in students]
print(passed_students2)
