# Using the print command in python.

# print('welcom to python 102!')
# print('welcom to python 101!')
# print('Create hammer')
# print('Create nails')
# print('Use hammer and nails')

# Variables

# failed_subjects = '2'
# name = 'John'

# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name + ' will need to redo ' + failed_subjects + ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')


# Data Types

failed_subjects = 2
name = 'John'

print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
print(name + ' will need to redo ' + str(failed_subjects) + ' courses.')
name = 'Eric'
print(name + ' is doing well in geography.')

print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

a = int(1)
b = int(2.5)
c = int("3")
d= int(float("3.4"))
e = float(1)
f = float(2.5)
g = float('3')
h = float('4.23')
i = str(22)
j = str(3.01)

print({
    "a should be 1": a,
    'b should be 2': b,
    'c should be 3': c,
    'd should be 3': d,
    'e should be 1.0': e,
    'f should be 2.5': f,
    'g should be 3.0': g,
    'h should be 4.23': h,
    'i should be "22"': i,
    'j should be "3.01"': j
})