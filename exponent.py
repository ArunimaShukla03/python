print(2**3)

#we may also use for loop to do the same

def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result *= base_num
  return result

print(raise_to_power(2,3))