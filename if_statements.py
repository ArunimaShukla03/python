is_male = False

#does not print the statement if its false otherwise prints the statement

if is_male:
  print("you are a male")
else:
  print("you are not a male")

# we may also use "or" keyword if either of the statements is true, the statement below it gets executed

is_female = True
is_tall = True

if is_female or is_tall:
  print("you are a female or tall or both")
else:
  print("you are neither female or tall")

  # we may use "and" keyword if both of the statements are true, the statement below it gets executed

  # elif is else-if statement

is_gay = True
is_happy = False

if is_gay and is_happy:
  print("I am happy for you.")
elif is_gay and not(is_happy):
  print("You have internalized homophobia.")
elif not(is_gay) and is_happy:
  print("You are homophobic.")
else:
  print("I am sorry")

# to return the largest of three numbers, we also use comparison operators such as !=, ==, <=, =>, <, >

def max_num(num1, num2, num3):
  if num1>=num2 and num1>=num3:
    return num1
  elif num2>=num1 and num2>=num3:
    return num2
  else:
    return num3
  
a=input("enter the first number: ")
b=input("enter the second number: ")
c=input("enter the third number: ")

print(max_num(a, b, c))