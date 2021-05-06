# zip(*iterables) = aggregate elements from two or more iterables
#                   creates a zip object witch paired elemants stored in tuples for each element

usernames = ('Dude', 'Bro', 'Mister')
passwords = ('p@ssword', 'abc', 'guest')
login_date= ('1/2/2021', '2/5/2020', '8/6/2018')

users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+' : '+value )

users_login = zip(users, passwords, login_date)

for i in users_login:
    print(i)