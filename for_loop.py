for a in "arunima":
  print(a)

friends=["jim","tim","him","kim"]
for a in friends:
  print(a)

#The last number is not included in range

for index in range(10):
  print(index)

for index in range(3,10):
  print(index)

for index in range(len(friends)):
  print(friends[index])

for index in range(5):
  if index == 0:
    print("first iteration")
  else:
    print("not first iteration")