#15. Squares 1–20
squares = [x**2 for x in range(1,21)]
print(squares)

#output-[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144,
#169, 196, 225, 256, 289, 324, 361, 400]


#16. Even numbers 1–50
evens = [x for x in range(1,51) if x%2==0]
print(evens)

#output-[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26,
#28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


#17. Words > 4 letters
words = ["apple","loki","beautiful","sun","python"]
long_words = [w for w in words if len(w)>4]
print(long_words)

#output-['apple', 'beautiful', 'python']


#18. 3x3 matrix

matrix = [[j for j in range(i,i+3)] for i in range(1,10,3)]
print(matrix)

#output- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#19. Replace negatives with 0

nums = [5,-3,7,-1,0,4]
new_list = [x if x>=0 else 0 for x in nums]
print(new_list)

#output-[5, 0, 7, 0, 0, 4]
