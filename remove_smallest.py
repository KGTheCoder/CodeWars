def remove_smallest(numbers):
  """
  smallest = numbers[0]
  for i in numbers:
    if i < smallest:
      smallest = numbers
  numbers.remove(smallest)
  return numbers
  """

  a = numbers[:]
  if a:
    a.remove(min(a))
  return a


print(remove_smallest([1,2,3,4,5]))