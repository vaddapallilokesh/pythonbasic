x = 10

def wrong_function():
    # Trying to modify global variable without declaring global
    x = x + 1   # This will raise UnboundLocalError
    print(x)

# Uncomment to see the error:
# wrong_function()

def correct_function():
    global x
    x = x + 1
    print("Fixed x =", x)

correct_function()

'''output-
Fixed x = 11
'''
