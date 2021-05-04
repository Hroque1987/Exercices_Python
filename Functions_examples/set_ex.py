

# set = collectio with is unordered, unindex. no duplicate values

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}
for x in utensils:
    print(x)
#utensils.add('napkin')
#utensils.remove('knife')
#utensils.clear()
#utensils.update(dishes)
#print(utensils)

dinner_table = utensils.union(dishes)
#print(dinner_table)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))
