def greet():
    return "Hello!"

# (a) Assign to new variable
say_hello = greet
print(say_hello())

# (b) Pass function as argument
def call_func(func):
    print("Calling:", func())

call_func(greet)

# (c) Return function from another function
def outer():
    def inner():
        return "Inner function called!"
    return inner

returned_func = outer()
print(returned_func())

'''output-
Hello!
Calling: Hello!
Inner function called!
'''
