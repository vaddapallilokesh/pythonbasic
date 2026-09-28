#Task 3: Variable-Length Arguments (*args)

def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print("3 Marks total and average:", total_marks(80, 90, 70))
print("5 Marks  total and average", total_marks(60, 75, 85, 90, 95))
print("1 Mark  total and average", total_marks(88))

'''output-
3 Marks total and average: (240, 80.0)
5 Marks  total and average (405, 81.0)
1 Mark  total and average (88, 88.0)
'''
