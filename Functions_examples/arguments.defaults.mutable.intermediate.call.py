def func(a= [], b= {}):
    print(a)
    print(b)
    print('#'* 3)
    a.append(len(a)) # this will affecte a's default value
    b[len(a)] = len(a) # and this will affect b's default value
    print(a)
    print(b)
    print('#'* 12)

func()
func(a=[1, 2, 3], b={'B': 1})
func()
