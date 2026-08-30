#6. Iterate dictionary

students = {101:"Lokesh", 102:"Sri", 103:"Hari"}

for k in students.keys():
    print("Key:", k)

for v in students.values():
    print("Value:", v)

for k,v in students.items():
    print(k,"->",v)

'''output-
Key: 101
Key: 102
Key: 103
Value: Lokesh
Value: Sri
Value: Hari
101 -> Lokesh
102 -> Sri
103 -> Hari'''


#7. Remove keys

students.pop(101)
print(students)
print(students.get(200,"Not Found"))

'''output-
{102: 'Sri', 103: 'Hari'}
Not Found
'''


#8. Check key exists

if 103 in students:
    print("Key 103 exists")

#output-Key 103 exists

    
#9. Merge dictionaries

d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4}
merged = d1.copy()
merged.update(d2)
print("Using update:", merged)
merged2 = d1 | d2
print("Using |:", merged2)

'''output-Using update: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Using |: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''


#10. Highest & lowest price

items = {"pen":10,"book":50,"pencil":5}
max_item = max(items,key=items.get)
min_item = min(items,key=items.get)
print("Highest:", max_item, items[max_item])
print("Lowest:", min_item, items[min_item])

'''output-
Highest: book 50
Lowest: pencil 5
'''

#11. Character frequency

text = "hello"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch,0)+1
print(freq)

#output-{'h': 1, 'e': 1, 'l': 2, 'o': 1}

#12. Dictionary comprehension

cubes = {x:x**3 for x in range(1,11)}
print(cubes)

#output-{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


