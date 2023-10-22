# Using the Print Stattement
print('hello', 'world')
# Indentation
if 5 > 4:
    print('5 is greater than 4')
# Creating Variables
x = 'hello'
y = 'world'
print(x,y)
print (x)
print (y)
# Slicing
x = 'python'
y = 'introduction'
print(x[2:5], y[:4])
# Modifying strings
x = 'hello world!'

print(x.upper()) # Change to uppercase
print(x.lower()) # Change to lower case
# Replacing string
print(x.replace('hello', 'hi'))
# Concatenate String (joining strings)
print(x + y) # to join without spacing
print(x + " " + y) # to join with space between the two variables
# Formating String
x = 23
y = 'My age is {}'
print(y.format(x))
# Python Operators
x = 2
y = 4
print(x+y) # Addition
print(x%y) # Modulos
print(y%x)
print(x**y) # Exponential
print(x//y)
print(y//x) # Floor Division
# Escape Characters
x = 'hello \n world' # New line
print(x)
x = '\'hello world\'' # Single quote
print(x)
x = '\\hello world\\' # Backlash
print(x)
x = 'hello\rworld' # Carriage return
print(x)