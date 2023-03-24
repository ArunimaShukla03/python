# Closure is an inner function that remembers and has access to variables in the local scope in which it was created even when the outer function is done executing.

def outer_func():
    message = 'Hi'

    def inner_func():

        # This inner function accesses this message variable. This is called a "free variable", as it is not defined in the inner function but we still have access to it.

        print(message)

    return inner_func()

outer_func()

def outer_func():
    message = 'Hi'

    def inner_func():

        print(message)

    return inner_func

my_func = outer_func()

# This "my_func" variable now is actually the inner function because that was what we actually returned.

print(my_func.__name__)

# This returns the name of the variable "my_func".

my_func()

# This actually executes the inner function. Thus "Hi" is printed.

# Now let's add parameters to the functions.

def outer_func(msg):
    message = msg

    def inner_func():

        print(message)

    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()