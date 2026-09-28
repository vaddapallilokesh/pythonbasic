#Task 4 Function Returning Multiple Values

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

nums = [5, 8, 12, 3, 9]
mn, mx, avg = stats(nums)
print("Min:", mn, "Max:", mx, "Average:", avg)

#output-
#Min: 3 Max: 12 Average: 7.4
