capitals = {'usa': 'washigton DC', 'india' : 'New Deli', 'russia': 'moskow'}

#print(capitals["russia"])

print(capitals.get('germany')) #much safer way, doesent return error on non exitante

#print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)
capitals.update({'germany':'berlin'})

capitals.update({'usa': 'las vegas'})

capitals.pop('india')
