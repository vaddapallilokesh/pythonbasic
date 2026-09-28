def factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))

'''output-
Factorial of 5: 120
Factorial of 0: 1
Factorial of -3: Invalid input
'''
