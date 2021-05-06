# sort() method = used with lists
# sort() function = used with iterables

students = [('Squidward', 'F',  60), #list of tuples
            ('Sandy', 'A', 33),
            ('Patrick', 'D', 36),
            ('Spongbob', 'B', 20),
            ('Mr. Krabs', 'C', 78)]

#students.sort() # sort by the first colum

#for i in students:
#    print(i)

grade = lambda grades:grades[1]
students.sort(key=grade,reverse=True)

for i in students:
    print(i)

age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)


# if it was a tuple of tuples or other iterable (including lists) 

#sorted_students = sorted(students,key=age)
#for i in sorted_students:
#    print(i)
