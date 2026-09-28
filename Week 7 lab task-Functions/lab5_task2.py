counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter =", counter)

for i in range(5):
    increment_counter()

'''output-
Counter = 1
Counter = 2
Counter = 3
Counter = 4
Counter = 5
'''


