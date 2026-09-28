def c_to_f(c):
    return (c * 9/5) + 32

temps_c = [0, 20, 30, 40]
temps_f = list(map(c_to_f, temps_c))
print("Temperatures in Fahrenheit:", temps_f)

words = ["apple", "banana", "grape"]
upper_words = list(map(str.upper, words))
print("Uppercase words:", upper_words)

'''output-
Temperatures in Fahrenheit: [32.0, 68.0, 86.0, 104.0]
Uppercase words: ['APPLE', 'BANANA', 'GRAPE']
'''
