def func(a= [], b= {}):
    print(a)
    print(b)
    print('#'* 12)
    a.append(len(a)) # this will affecte a's default value
    b[len(a)] = len(a) # and this will affect b's default value

func()
func()
func()
