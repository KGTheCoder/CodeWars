"""
def descending_order(nums):
  nums.sort(reverse=True)
  print(nums)

nums = [4, 2, 1, 4, 5]
descending_order(nums)
"""

"""
num = 42145
num2 = str(num)
list1 = list(num2)
list2 = sorted(list1, reverse=True)
string1 = ''.join(list2)
final_value = int(string1)
print(final_value)
"""

"""
def Descending_Order(num):
  return int("".join(sorted(str(num), reverse=True)))

print(Descending_Order(42145))
"""

"""
def Descending_Order(num):
  # Grab each element from num and store each value as a string in a list
  li = [x for x in str(num)]
  # Sort the list in descending order
  li.sort(reverse=True)
  # Convert list to string, then return as int
  return int(''.join(x for x in li))

print(Descending_Order(42145))
"""

"""
def Descending_Order(num):
  num = list(str(num))
  num.sort(reverse=True)

  result = ''

  for i in num:
    result += i
  
  return(int(result))

print(Descending_Order(42145))
"""