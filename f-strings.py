
# %s is used to incorporaate another string within a string. This is one type of string formtting but this becomes incovenient when we are dealing with very long strings.

me = "Arunima"
a = "this is %s"%me
print(a)

# Tuples can also be used in string formatting but this also becomes incovenient incase of very long strings.

me = "Arunima"
a1 = 18
a = "this is %s and i am %s years old."%(me,a1)
print(a)

# Dot format is also another method of string formatting.

me = "Arunima"
a1 = 18
a = "This is {} and I am {} years old."
b = a.format(me, a1)
print(b)

# This can also be used by writing the indices of the tuple.

me = "Arunima"
a1 = 18
a = "This is {1} and I am {0} years old."
b = a.format(me, a1)
print(b)

# But this is also inconvenient for longer strings.

# Therefore, F-string is introduced which is a new method of string formatting.

me = "Arunima"
a1 = 18
a = f"this is {me} and I am {a1} years old."
print(a)

# We may also use variable expressions and modules such as

b = f"this is {me} and I am {a1} years old. I have {2*2} cats."
print(b)