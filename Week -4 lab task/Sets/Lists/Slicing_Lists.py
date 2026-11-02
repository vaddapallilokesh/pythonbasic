#6. Slicing examples

nums = [1,2,3,4,5,6,7,8,9,10]
print("First 3:", nums[:3])
print("Last 3:", nums[-3:])
print("Alternate:", nums[::2])

'''First 3: [1, 2, 3]
Last 3: [8, 9, 10]
Alternate: [1, 3, 5, 7, 9]
'''

#7. Reverse using slicing
nums = [1,2,3,4,5]
print("Reversed:", nums[::-1])

#output-Reversed: [5, 4, 3, 2, 1]

#8. Middle 4 elements
nums = list(range(1,13))  
print("Middle 4:", nums[4:8])

#oiutput-Middle 4: [5, 6, 7, 8]
