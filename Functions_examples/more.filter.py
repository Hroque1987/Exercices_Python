s = list(range(int(input('Number to check:'))))

def bigger_than(n):
    if n > 20:
        return True
    else:
        return False

bigger = filter(bigger_than, s)

for i in bigger:
    print(i)
