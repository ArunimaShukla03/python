# Decorators are function that takes another function as an argument, adds some kind of functionality and returns another function. All of this is done without altering the source code of the original function that we passed in.

def decorator_func(original_func):

    def wrapper_func():
        return original_func()

    return wrapper_func

