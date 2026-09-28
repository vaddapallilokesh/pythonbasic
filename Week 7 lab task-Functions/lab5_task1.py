counter = 0  # global variable

def show_local():
    counter = 5  # local variable
    print("Local counter inside function:", counter)

show_local()
print("Global counter outside function:", counter)

'''output-
Local counter inside function: 5
Global counter outside function: 0
'''
