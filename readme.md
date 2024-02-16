## Decorator

#### What is a Decorator?

In Python, a decorator is a design pattern that allows behavior to be added to functions or classes dynamically. Decorators are implemented as callable objects (functions) that accept another function as input and return a new function that usually extends or modifies the behavior of the original function without changing its source code.

#### How Decorators are Used in Python

Decorators are commonly used for:
- Adding functionality to functions or methods without modifying their original code.
- Wrapping functions with pre- or post-processing behavior.
- Validating inputs or outputs.
- Timing functions, as in the case of the `timeit` decorator.

#### How the Decorator is Used in This Code

The `timeit` decorator in this code measures the execution time of a function. Here's how it works:

1. **Definition of the `timeit` Decorator**: The `timeit` decorator is defined as a function that takes another function (`func`) as input.

2. **The Wrapper Function**: Inside the `timeit` decorator, a wrapper function (`wrapper`) is defined. This wrapper function takes any number of positional and keyword arguments (`*args` and `**kwargs`), which allows it to be generic and work with any function.

3. **Timing the Function Execution**: Inside the wrapper function, the current time is recorded (`start_time`) just before calling the original function (`func`). Then, the original function (`func`) is called with the provided arguments (`*args` and `**kwargs`). After the function execution, another timestamp is recorded (`end_time`).

4. **Calculating and Printing Execution Time**: The difference between the end time and the start time is calculated to determine the execution time of the function. This duration is printed to the console, indicating the time taken for the function to execute.

5. **Returning the Result**: Finally, the result of calling the original function is returned from the wrapper function.

6. **Using the Decorator**: To use the `timeit` decorator, simply decorate the desired function with `@timeit` above its definition. When the decorated function is called, it will automatically measure and print its execution time.

#### Example Usage

```python
@timeit
def some_function():
    # Your code here
    pass

some_function()
```

This will output the execution time of `some_function()` in seconds when it is called.