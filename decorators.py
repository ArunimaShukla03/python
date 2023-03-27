# Decorators are function that takes another function as an argument, adds some kind of functionality and returns another function. All of this is done without altering the source code of the original function that we passed in.

def decorator_func(original_func):

    def wrapper_func():
        return original_func()
    
    # This wrapper function is waiting to be executed.

    return wrapper_func

def display():
    print("display function ran")

decorated_display = decorator_func(display)

decorated_display()

# Decorators allows us to easily add functionality to our existing functions by adding that functionality inside the wrapper function.

def decorator_func(original_func):

    def wrapper_func():

        print("wrapper excuted this before {}".format(original_func.__name__))

        return original_func()

    return wrapper_func

def display():
    print("display function ran")

decorated_display2 = decorator_func(display)

decorated_display2()

# Instead of assigning these again and again to different variables and executing them, we can simply write "@decorator_func" above the display function to do the exact same thing.

@decorator_func
def printout():
    print("decoratorsss")

printout()

# We can not add "@decorator_func" before this as it gives an error saying that the wrapper_func takes 0 arguments and here two arguments were given.Thus we can pass in any arbitrary number of arguments in the wrapper_func by adding "*args" and "**kwargs" for your functions. 

def decorator_function(original_func):
    
    def wrapper_function(*args, **kwargs):

        print("wrapper function is executed this before {}".format(original_func.__name__))

        return original_func(*args, **kwargs)

    return wrapper_function

@decorator_function
def display_info(name, age):

    print("print display_info ran with arguments({}, {})".format(name,age))

display_info("John", 30)

display()

# This display function is being executed.