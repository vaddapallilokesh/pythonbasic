def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@log_call
@timer
def multiply(a, b):
    return a * b

multiply(4, 5)

'''output-
Calling wrapper with (4, 5), {}
multiply took 0.0000 seconds
wrapper returned 20
'''
