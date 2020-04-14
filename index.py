# Using the print command in python.

# print('welcom to python 102!')
# print('welcom to python 101!')
# print('Create hammer')
# print('Create nails')
# print('Use hammer and nails')

# Working with Variables

# failed_subjects = '2'
# name = 'John'

# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name + ' will need to redo ' + failed_subjects + ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')


# Working with Datatypes

# failed_subjects = 2
# name = 'John'

# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
# print(name + ' will need to redo ' + str(failed_subjects) + ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')

# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))

# a = int(1)
# b = int(2.5)
# c = int("3")
# d= int(float("3.4"))
# e = float(1)
# f = float(2.5)
# g = float('3')
# h = float('4.23')
# i = str(22)
# j = str(3.01)

# print({
#     "a should be 1": a,
#     'b should be 2': b,
#     'c should be 3': c,
#     'd should be 3': d,
#     'e should be 1.0': e,
#     'f should be 2.5': f,
#     'g should be 3.0': g,
#     'h should be 4.23': h,
#     'i should be "22"': i,
#     'j should be "3.01"': j
# })

# Variables and Datatypes Exercise

#Create appropriate variables for items name, the price and hom many you have in stock.

# itme_name = 'bulb'
# price = 9.99
# inventory = 120
# is_in_inventory = True

# print(itme_name,price,inventory, is_in_inventory)

# Working with Arithmetic Operations

# a = 10
# b = 3

# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float)  : ', a / b)
# print('Division (floor)  : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# Working with Strings

msg = 'welcome to python 101 : Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# print(len(msg))
# print(msg.count('t'))
# slicing string into characters
# print(msg[:5])


new_string = msg[18] + ' ' + msg[:8] + msg[-5:-1]+ msg[7:11] + msg[13] + msg[12] + msg[2] + msg[6] + msg[-5]
print(new_string.title())
print(new_string[::-1].title())