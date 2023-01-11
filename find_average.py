def find_average(numbers):
  """
  num_sum = 0
  for i in numbers:
    num_sum += i
  return int(num_sum / len(numbers))
  """

  # return sum(numbers) / len(numbers) if numbers else 0
  # return sum(numbers) / len(numbers)
  try:
    return sum(numbers) / len(numbers)
  except ZeroDivisionError:
    return 0

print(find_average([1, 2, 3]))