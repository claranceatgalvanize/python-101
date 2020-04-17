# WORKING THE PRINT METHOD ######################################

# print('welcom to python 102!')
# print('welcom to python 101!')
# print('Create hammer')
# print('Create nails')
# print('Use hammer and nails')

# WORKING WITH VARIABLES ########################################

# failed_subjects = '2'
# name = 'John'

# print('Dear Mrs Badger')
# print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
# print(name + ' will need to redo ' + failed_subjects + ' courses.')
# name = 'Eric'
# print(name + ' is doing well in geography.')


# WORKING WITH DATATYPES #######################################

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

# Variables and Datatypes Exercise ------------------------------

#Create appropriate variables for items name, the price and hom many you have in stock.

# itme_name = 'bulb'
# price = 9.99
# inventory = 120
# is_in_inventory = True
# print(itme_name,price,inventory, is_in_inventory)

#WORKING WITH ARITHMETIC OPERATIONS #############################

# a = 10
# b = 3

# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float)  : ', a / b)
# print('Division (floor)  : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# WORKING WITH STRINGS ##########################################

# msg = 'welcome to python 101 : Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# print(len(msg))
# print(msg.count('t'))
# slicing string into characters
# print(msg[:5])


# new_string = msg[18] + ' ' + msg[:8] + msg[-5:-1]+ msg[7:11] + msg[13] + msg[12] + msg[2] + msg[6] + msg[-5]
# print(new_string.title())
# print(new_string[::-1].title())

# Find and Replace, String Formating ---------------------------

# msg = """Dear Terry,, 
# You must cut down the mightiest
# tree in the forest with...
# a herring! <3"""

# msg1 = 'Welcome to Python 101: Strings'
# msg2 = msg1.replace('Python', 'Java')
# print(msg2)
# print('Python' in msg1)

# name = 'CLARANCE'
# color = 'RED'
# msg3 = '[' + name +'] loves the color ' + color + '!'
# msg4 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg3)
# print(msg4)

# WORKING WITH USER INPUTS ####################################
# name = input('What is your name?: ')
# age = input('What is your age?: ')
# print(f'Hello {name}! You are {age} years old.') 

# num1 = input('Enter a digit: ')
# num2 = input('Enter a second digit: ')
# ans = float(num1) + float(num2)
# print(ans)

# User Input Exercise
# name = input('What your name?: ')
# distance_km = input('What kilometer would like to convert?: ')
# distance_mi = float(distance_km) * 0.62137
# print(f'Hello {name.capitalize()}! your distance is {distance_mi} miles')


# WORKING WITH LIST ###########################################

# friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham'] # creating a list

# ACCESSING LIST ELEMENTS -------------------------------------

# accessing list elements
# print(friends[1], friends[4])
# print(friends[2:4]) 
# print(friends[:3])  
# print(friends[:]) 
# print(len(friends)) # get list lenght
# print(friends.index('Eric')) # get Eric's index
# print(friends.count('Eric')) # number of occurences of eric

# cars = [911, 130, 328, 535, 740, 308]

# print(friends)
# print(cars)

# SORTING A LIST ----------------------------------------------

# friends.sort()# sorts list top to bottom
# print(friends) 
# friends.sort(reverse = True) # sorts list bottom to top
# print(friends) 
# friends.reverse() # reverses the order of the list
# print(friends)

# print(min(friends)) # output the smallest element
# print(max(friends)) # output the largest element
# print(min(cars)) # output the smallest element
# print(max(cars)) # output the largest element
# print(sum(cars)) # sums up the elements of the list

# ADDING ELEMENTS TO A LIST -----------------------------------

# friends.append('Terry') # adds an el at the end of a list
# friends.insert(1, 'TerryG') # puts an el at a specific index in a list
# friends[2]='Clarance' # puts an el at a specific index in a list
# friends.extend(cars) # merges multiple lists
# print(friends)

# REMOVING ELEMENTS FROM A LIST -------------------------------

# friends.remove('TerryG')
# friends.pop()
# friends.clear()
# del friends[1]
# print(friends)

# COPYING A LIST -------------------------------

# new_friends = friends.copy()
# new_friends = list(friends)
# new_friends = friends[:]

# print('new friends: ', new_friends)


# LIST EXERCISE --------------------------------

# sales_w1 = [7, 3, 42, 19, 15, 35, 9]
# sales_w2 = [12, 4, 26, 10, 7, 28]
# sales = []

# new_day = input('Enter a digit')
# sales_w2.append(int(new_day))

# # sales.extend(sales_w1)
# # sales.extend(sales_w2)

# sales = sales_w1 + sales_w2

# sales.sort()

# print(sales)
# worse_day_prof = sales[0] * 1.5
# best_day_prof = sales[-1] * 1.5
# combined_day_prof = worse_day_prof + best_day_prof

# print(f'Best day profit: {worse_day_prof}')
# print(f'Worse day profit: {best_day_prof}')
# print(f'Combined profit: {combined_day_prof}')

# WORKING WITH SPLIT AND JOIN ##################################

# msg ='Welcome   to   Python   101:   Split   and   Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']

# character_list = list(msg)
# word_list = msg.split()
# csv_split = csv.split(',')

# friend = '--'.join(friends_list)

# join_msg = msg.replace(' ', '-')
# print(join_msg)

# SPLIT AND JOIN EXERCISE --------------------------------------

# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
# names = csv.replace(';', ',')
# names = names.replace(':', ',')
# names = names.split(',')

# friends_list = names[:]

# print('')
# print(names)
# print('')
# print('Friends: ',friends_list)

# WORKING WITH TUPLE ##################################

# TUPLE DEFINATION ------------------------------------
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# friends_tuple = 'gus'
# print(friends_tuple)

