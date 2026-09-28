def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def reverse_number(n):
    def helper(n, rev):
        if n == 0:
            return rev
        return helper(n // 10, rev * 10 + n % 10)
    return helper(n, 0)

print("Sum of digits of 1234:", sum_of_digits(1234))
print("Reverse of 1234:", reverse_number(1234))

'''output-
Sum of digits of 1234: 10
Reverse of 1234: 4321
'''
