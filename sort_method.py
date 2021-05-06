# sort() method = used with lists
# sort() function = used with iterables

students = ['Squidward', 'Sandy', 'Patrick', 'Spongbob', 'Mr. Krabs']

#students.sort(reverse=True) # Onlu works with lists

#for i in students:
#    print(i)


sorted_students = sorted(students, reverse=True) # works with other iterabels

for i in sorted_students:
    print(i)



