#4. Union, intersection, difference

a = {1,2,3,4}
b = {3,4,5,6}
print("Union:", a|b)
print("Intersection:", a&b)
print("Difference:", a-b)
print("Symmetric Difference:", a^b)

'''output-
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}
'''
#5. Subset & superset

a = {1,2}
b = {1,2,3,4}
print("a subset of b:", a.issubset(b))
print("b superset of a:", b.issuperset(a))

'''output-
a subset of b: True
b superset of a: True
'''


#6. Remove vs discard

s = {1,2,3}
s.remove(2)   # removes element, error if not found
s.discard(5)  # no error if not found
print(s)

#output-{1, 3}


#7. Disjoint sets

a = {1,2}
b = {3,4}
print("Disjoint:", a.isdisjoint(b))

#output-Disjoint: True


#8. Unique sorted list

nums = [1,2,2,3,4,4,5]
unique = set(nums)
sorted_list = sorted(unique)
print(sorted_list)

#output- [1, 2, 3, 4, 5]


#9. Set comprehension

squares = {x**2 for x in range(1,21) if x%2!=0}
print(squares)

#output- {1, 121, 225, 289, 9, 169, 361, 81, 49, 25}



 	 

