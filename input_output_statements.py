# 1. User's name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you will turn {age+1} next year.")

'''
Enter your name: Lokesh
Enter your age: 20
Hello Lokesh, you will turn 21 next year.'''


# 2. Two numbers as strings, then convert and calculate
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

a = int(num1)
b = float(num2)

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)

'''Enter first number: 10
Enter second number: 20
Sum = 30.0
Difference = -10.0
Product = 200.0
Quotient = 0.5'''


# 3. Output formatting methods
student_name = "Lokesh"
marks = 95

print(student_name, marks)                           
print("Name: {}, Marks: {}".format(student_name, marks))  
print(f"Name: {student_name}, Marks: {marks}")

'''Lokesh 95
Name: Lokesh, Marks: 95
Name: Lokesh, Marks: 95'''


# 4. Multiple values in one line, sum
values = input("Enter numbers separated by spaces: ")
nums = list(map(int, values.split()))
print("Sum =", sum(nums))

'''Enter numbers separated by spaces: 10 20 30
Sum = 60'''


# Average of 3 subject marks
marks_input = input("Enter 3 subject marks separated by spaces: ")
marks_list = list(map(int, marks_input.split()))
average = sum(marks_list) / len(marks_list)
print(f"Average = {average:.2f}")

'''
Enter 3 subject marks separated by spaces: 80 90 100
Average = 90.00
'''
