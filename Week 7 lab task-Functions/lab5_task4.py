def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = make_counter()
print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

'''output-
1
2
3
'''
