from functools import reduce

nums = [2, 4, 6, 8]

product = reduce(lambda a, b: a * b, nums)
maximum = reduce(lambda a, b: a if a > b else b, nums)
sentence = reduce(lambda a, b: a + " " + b, ["Python", "is", "fun"])

print("Product:", product)
print("Maximum:", maximum)
print("Sentence:", sentence)


'''output-
Product: 384
Maximum: 8
Sentence: Python is fun
'''
