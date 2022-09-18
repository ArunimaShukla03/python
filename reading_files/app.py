#we may read files in different modes such as "r", "w", "a" (you can't modify or change any information in the file but you may append it or add information at the end of the file), "r+" (this is used to both read and write information in the file)

employee_file = open("reading_files/employees.txt", "r")

#to check wheather we can read a file or not we can use ".readable()"

print(employee_file.readable())

#to spit out all the information from a file, we may use ".read()"

'''print(employee_file.read())'''

#to read individual line of the file, use ".readline()"

'''print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())'''

#to read lines and put them in an array, we use ".readlines()"

'''print(employee_file.readlines())'''

#we may access individual elements by the usage of for loop as well

for employee in employee_file.readlines():
  print(employee)

#In case, we want to access individual elements in the array, we should use index

'''print(employee_file.readlines()[1])'''

#whenever you open a file, it is also essential to close that file as well

employee_file.close()