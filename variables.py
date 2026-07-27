# 1. Declare variables and print with types
name = "LOkesh"
age = 1
height = 5.2
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

'''LOkesh <class 'str'>
1 <class 'int'>
5.2 <class 'float'>
True <class 'bool'>'''



# 2. Multiple assignment
a, b, c = 10, 20, 30
print("a, b, c =", a, b, c)

a = b = c = 100
print("a, b, c =", a, b, c)

'''a, b, c = 10 20 30
a, b, c = 100 100 100'''


# Swapping values
# (a) Using a temporary variable
x, y = 5, 7
temp = x
x = y
y = temp
print("Swap with temp:", x, y)

#output-Swap with temp: 7 5


# (b) Using tuple unpacking
x, y = 5, 7
x, y = y, x
print("Swap with tuple:", x, y)

#output-Swap with tuple: 7 5


# 3. Dynamic typing
var = 42
print(var, type(var))
var = "Now I'm a string"
print(var, type(var))

'''output-42 <class 'int'>
Now I'm a string <class 'str'>'''

