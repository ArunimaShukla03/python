# Closure is a 

def outer_func():
    message = 'Hi'

    def inner_func():

        # This inner function accesses this message variable.
        
        print(message)

    return inner_func()

outer_func()