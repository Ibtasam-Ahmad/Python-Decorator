import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# Example usage
@timeit
def some_function():
    # Basic code
    for i in range(0, 1000000):
        pass

some_function()
