#4. Indexing

tpl = (10,20,30,40,50,60,70,80,90,100)
print("Index 0:", tpl[0])
print("Index 5:", tpl[5])
print("Last:", tpl[-1])

'''output-
Index 0: 10
Index 5: 60
Last: 100
'''


#5. Slicing halves

tpl = tuple(range(1,13))
print("First half:", tpl[:6])
print("Second half:", tpl[6:])

'''output-
First half: (1, 2, 3, 4, 5, 6)
Second half: (7, 8, 9, 10, 11, 12)
'''


#6. Value exists

tpl = (1,2,3,4,5)
print(3 in tpl)
print(10 in tpl)

'''output-
True
False
'''


#7. Max, Min, Count

tpl = (5,8,2,8,3,8)
print("Max:", max(tpl))
print("Min:", min(tpl))
print("Count of 8:", tpl.count(8))

'''output-
Max: 8
Min: 2
Count of 8: 3
'''

