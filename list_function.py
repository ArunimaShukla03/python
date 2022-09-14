lucky_numbers = [5, 5, 56, 89, 8, 10, 12]
friends=["arunima","baby","cat","dog","elephant"]
print(friends)

#remove a particular element from the list
friends.remove("dog")
print(friends)

#pop element is used to pop the last element off of the list
friends.pop()
print(friends)

#finding out the index of a particular element
print(friends.index("arunima"))

#remove all the elements from the list
friends.clear()
print(friends)

#count element is used to find how many times an element is used in a string
print(lucky_numbers.count(5))

#sort is used to sort the elements in the list
lucky_numbers.sort()
print(lucky_numbers)

#reverse is used to reverse the order of the elements in the list
lucky_numbers.reverse()
print(lucky_numbers)

#copy is used to copy the exact list
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers)