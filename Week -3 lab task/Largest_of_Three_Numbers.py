x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y:
    if x >= z:
        print("Largest:", x)
    else:
        print("Largest:", z)
else:
    if y >= z:
        print("Largest:", y)
    else:
        print("Largest:", z)


'''output-
   Enter first number: 67
   Enter second number: 89
   Enter third number: 35
   Largest: 89'''
