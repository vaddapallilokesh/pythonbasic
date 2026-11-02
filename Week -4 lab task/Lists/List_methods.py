#11. Demonstrating methods

lst = [10,20,30]
lst.append(40)
print("After append:", lst)
lst.insert(1,15)
print("After insert:", lst)
lst.extend([50,60])
print("After extend:", lst)
lst.remove(20)
print("After remove:", lst)
lst.pop()
print("After pop:", lst)
lst.sort()
print("After sort:", lst)
lst.reverse()
print("After reverse:", lst)

print("Count of 30:", lst.count(30))
print("Index of 15:", lst.index(15))

'''output-
After append: [10, 20, 30, 40]
After insert: [10, 15, 20, 30, 40]
After extend: [10, 15, 20, 30, 40, 50, 60]
After remove: [10, 15, 30, 40, 50, 60]
After pop: [10, 15, 30, 40, 50]
After sort: [10, 15, 30, 40, 50]
After reverse: [50, 40, 30, 15, 10]
Count of 30: 1
Index of 15: 3'''


#12. Remove duplicates (without set)

nums = [1,2,2,3,4,4,5]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
print("Without duplicates:", unique)

#output-Without duplicates: [1, 2, 3, 4, 5]


#13. Max, Min, Sum manually

nums = [5,8,2,10,3]
maximum = nums[0]
minimum = nums[0]
total = 0

for n in nums:
    if n > maximum:
        maximum = n
    if n < minimum:
        minimum = n
    total += n

print("Max:", maximum)
print("Min:", minimum)
print("Sum:", total)

'''output-
Max: 10
Min: 2
Sum: 28'''


#14. Merge + sort descending

a = [5,2,9]
b = [1,7,3]
merged = a + b
merged.sort(reverse=True)
print("Merged & Descending:", merged)

#output-Merged & Descending: [9, 7, 5, 3, 2, 1]

