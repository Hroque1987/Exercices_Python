try:
    numerator = int(input('Enter a number:'))
    denominator = int(input('Enter a number to divide by:'))
    result = numerator / denominator

    

except ZeroDivisionError as e:
    print(e)
    print('You cant divide by zero')
except ValueError as e:
    print(e)   
    print('Enter numbers only')
except Exception as e:
    print(e)
    print('Something went wrong')
else:
    print(result)
finally:
    print('This will always execute')
