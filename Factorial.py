num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)

'''output-
Enter a number: 5
Factorial of 5 is 120
'''
