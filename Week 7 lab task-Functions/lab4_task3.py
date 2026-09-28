students = [("Ram", 78), ("Sita", 92), ("laxman", 65)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Sorted by marks:", sorted_students)

words = ["apple", "banana", "kiwi", "grape"]
sorted_words = sorted(words, key=lambda w: len(w))
print("Sorted by length:", sorted_words)

'''output-

Sorted by marks: [('Sita', 92), ('Ram', 78), ('laxman', 65)]
Sorted by length: ['kiwi', 'apple', 'grape', 'banana']
'''
