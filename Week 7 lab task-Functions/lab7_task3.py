import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def heavy_task():
    total = sum(range(1, 1000000))
    return total

heavy_task()

'''output-
heavy_task took 0.00771 seconds
'''
