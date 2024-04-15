
#print(2 + 3) # Addition(+)
#print(3 - 1) # Subtraction(-)
#print(2 * 3) # Multiplication(*)
#print(3 / 2 ) # Division (/)
#print(3 ** 2) # Exponential (**)
#print(3 % 2) # Modulus(%)
#print(3 // 2) # Floor division operator(//) -> Division without decimal points 

# Checking data types 
#print(type(10)) # Prints int 
#print(type(3.1)) # Prints float 
#print(type (1 + 3j)) # prints complex 
#print(type([1, 2, 3])) # prints list 
#print(type({'name': 'Raymond Donkemezuo'})) # Dictionary of key/value pair
#print(type({9.8, 3.142, 2.7})) # prints set of float numbers 
#print(type((9.8, 3.14, 2.7))) # prints tuple

# Variables in Python 
#first_name = 'Raymond'
#last_name = 'Donkemezuo'
#print(type(first_name)) # Checks the data type of the first name variable. Print str
#print('First name: ', first_name) # printing value stored in variable 
#print('Last name: ', last_name) # printing value stored in variable 

# Declaring multiple variables in a single line 
# The multiple variables does not have to be of the same data type
#country, state, lga, chairman = 'Nigeria', 'Bayelsa', 'Kolga', 'Inoru'
#print(country)
#print(state)
#print(lga)
#print(chairman)

# Asking user for input 
# first_name = input('what is your name: ')
# age = input('How old are you: ')

# print(first_name)
# print(age)
# print(len(first_name)) # checks the length of the first name variable

radius = 30
area = 3.142 * (radius ** 2)
#print(area)
#print(c)

# userInputRadius = input('Enter radius: ')
# userInputInt = int(userInputRadius)
# calculatedArea = 3.142 * (userInputInt ** 2)
#print(calculatedArea)

# Slicing Strings in Python 
language = 'Python'
# Accessing the first three characters of a string 
first_three = language[0:3] # characters in the index range of 0..2
print(first_three) # Prints Pyt 

last_three = language[3:] # the remaining characters of the string with element at index 3 inclusive
print(last_three) # hon

last_three_method_2 = language[-3:] # the last 3 characters of a string 
print(last_three_method_2) # hon 

# To reverse a string 
greeting = 'Hello, world!'
print(greeting[::-1]) # !dlrow ,olleH

# Skipping while slicing 
pto = language[0:6:2] # Skipping 1 after every character 
print(pto)

# Counting substring occurence in a string 
challenge = 'thirty days of python'
print(challenge.count('y'))

# Checks if a string ends with a substring 
print(challenge.endswith('on')) # true: Checks if string ends with substring 'on'
print(challenge.endswith('tion')) # false:  Checks if string ends with substring 'tion'

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs) # replaces tab character with spaces 

# Find - Returns the index of the first occurence of a substring, if not found - return -1 
first_index_of_y = challenge.find('t') # Prints out the first index of y in the string 
print(first_index_of_y)

# rfind - Returns the index of the last occurrence of a substring, if not found - return -1 
last_index_of_y = challenge.rfind('y')
print(last_index_of_y)

# index() -> Returns the lowest index of the substring 
# rindex() -> Returns the highest index of the substring 
# isalnum() -> Checks alphanumeric character 
# isalpha() -> Return true if all characters in the string are alphabet characters (A - Z)
# isdecimal() -> Returns true if all characters in the string are decimals (0-9)
# isdigit() -> Returns true if all characters in the string are integers and other unicode characters for numbers


# List in Python 

# Empty list 
emptyList = list() 

# Getting the length of a list 
length = len(emptyList) # 0 

print(length)

# Initializing list using square brackets 
emptyList = [] # An empty list 

print(len(emptyList))

# List can contain objects of different data types 
myList = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # A list containing str, int, bool, dictionary
print(myList)

# Accessing list items using positive index. Indexes start from 0 to length - 1
# Accessing list items using negative index means beginning from the end. -1 referes to the last element on the list

# Check if an item is contained in a list 
fruits = ['banana', 'orange', 'mango', 'lemon', 'grape']
does_exist = 'banana' in fruits # Checks if banana is contained in the list. 'does_exist' is a boolean variable

# Removing items from a list 

# 1. Removing a specific item from a list 
# fruits.remove('orange') # Removes orange from the list 

# 2. Remove item using Pop - Pop() removes the last element / Pop(index) removes at a particular index 
# fruits.pop() # Removes the last element on the list 
# print(fruits)

# Remove item using Del
#del fruits[0] # removes the first element 
# print(fruits)

# Clearing a list 
# fruits.clear()
print(fruits)