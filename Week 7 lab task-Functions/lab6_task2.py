def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

nums = list(range(1, 51))
primes = list(filter(is_prime, nums))
print("Prime numbers:", primes)

words = ["madam", "apple", "level", "banana", "radar"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print("Palindromes:", palindromes)

'''output-
Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Palindromes: ['madam', 'level', 'radar']
'''
