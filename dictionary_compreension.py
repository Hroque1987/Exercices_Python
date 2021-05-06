# dictionary compreension = create dictionaries using an expression
#                           can replace for loops and certain lambda function

# dictionary compreesion = {key: expression for (key, value) in iterable}

cities_in_F = {'New York' : 32,
                'Boston' : 75,
                'Los Angeles' : 100,
                'Chicago' : 50 }


cities_in_C = {key: round(((value-32)*(5/9))) for (key, value) in cities_in_F.items()}

print(cities_in_C)


# dictionary = {key: expression for (key,value) in iterable if conditional}

weather = {'New York' : 'snowing',
            'Boston' : 'sunny',
            'Los Angeles' : 'sunny',
            'Chicago' : 'cloudy' }

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}

print(sunny_weather)

# dictionary = {key: (if/else) for (key,value) in iterable}

cities = {'New York' : 32,
                'Boston' : 75,
                'Los Angeles' : 100,
                'Chicago' : 50 }

desc_cities ={key: ('warm ' if value >= 40 else 'cold') for (key,value) in cities.items() }

print(desc_cities)

# dictionary = {key: function(value) for (key,value) in iterable}

cities_2 = {'New York' : 32,
                'Boston' : 75,
                'Los Angeles' : 100,
                'Chicago' : 50 }

def check_temp(value):
    if value >= 70:
        return 'Hot'
    elif 69 >= value >= 40:
        return 'Warm'
    else:
        return 'Cold'


func_cities ={key: check_temp(value) for (key,value) in cities_2.items() }

print(func_cities)