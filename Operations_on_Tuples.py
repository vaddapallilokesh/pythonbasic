#8. Concatenate + repeat

a = (1,2,3)
b = (4,5)
print("Concatenated:", a+b)
print("Repeated:", a*3)

'''output-
Concatenated: (1, 2, 3, 4, 5)
Repeated: (1, 2, 3, 1, 2, 3, 1, 2, 3)
'''

#9. Unpack marks

marks = (80,75,90,85,70)
m1,m2,m3,m4,m5 = marks
avg = (m1+m2+m3+m4+m5)/5
print("Average:", avg)

#output-Average: 80.0


#10. Tuple immutability

tpl = (1,2,3)
try:
    tpl[0] = 10
except TypeError as e:
    print("Error:", e)

#output- Error: 'tuple' object does not support item assignment    

    
#11. Nested list inside tuple

tpl = (1, [2,3], 4)
tpl[1].append(5)
print(tpl)

#output- (1, [2, 3, 5], 4)
# Explanation: Tuples are immutable, but the list inside is mutable.


#12. Sort tuple

tpl = (5,2,9,1)
sorted_list = sorted(tpl)
print("Sorted list:", sorted_list)

#output- Sorted list: [1, 2, 5, 9]
