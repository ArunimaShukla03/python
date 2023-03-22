# First-class functions refer to the ability of a programming language to treat functions as first-class citizens, just like any other variable or data type. This means that function can be assigned to variables, passed as arguments to other functions and returned as values from functions.

def square(x):
    return x*x

f = square(5)

print(square)
print(f)

# By this point, after running the function it is printing out both <function square at 0x7fab75eb84a0> and 25. 

# Next, we won't write paranthesis as it means that we are executing the function which we are not. We just wanna set our variable "a" to the function and not execute it.

a = square

print(a)

# Now, this prints out <function square at 0x7f16db1984a0>

# Hence, we can treat "a" now just like we treat "square".

print(a(5))

# This prints 25. 

# Till now, we only assigned functions to variables but we can also pass functions as arguments and return functions as the result of other functions.

# We also have the concept of "higher order functions" which are the functions that take other functions as their arguments or return a function as a result.

def my_map(func, array):

    result = []

    for i in array:
        result.append(func(i))

    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)

# Now we need to return a function from another function.

def logger(msg):

    def log_message():
        print('Log:', msg)

    # Here we have no paranthesis so that function doesn't execute at that time.

    return log_message

log_hi = logger('Hi')

# Now this is returning the "log_message" function with the msg in it as "Hi".

# Thus, we simply execute this function where previous "log_hi" value is retained.

log_hi()

# This prints "Log: Hi".

def html_tag(tag):

    def wrap_text(msg):

        # It prints out the tag, then the msg and then the tag.

        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')

# It stores the "tag" as h1 and wrap_text is not executed yet.

print_h1('Test Headline!')

# Now we pass in "msg" argument.

print_h1('Another Headline!')

# Now it stores the "tag" as p and wrap_text is not executed yet.

print_p = html_tag('p')
print_p('Test Paragraph!')