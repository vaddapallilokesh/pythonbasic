#Task 3: Even or Odd Checker

def is_even(n):
    return n % 2 == 0

numbers = [10, 7, 4, 9, 2]
for num in numbers:
    if is_even(num):
        print(num, "is Even")
    else:
        print(num, "is Odd")


'''output-
10 is Even
7 is Odd
4 is Even
9 is Odd
2 is Even

'''
