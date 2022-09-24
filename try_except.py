try:
  answer=10/0
  number= int(input("Enter a number: "))
  print(number)
except ZeroDivisionError as err:
  print(err)
except ValueError:
  print("Invalid input.")

#only writing "except" is way too broad, hence we should always define the type of error which we may come across.

