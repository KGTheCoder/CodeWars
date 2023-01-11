def square_sum(numbers):
  # return [n += n*n for n in numbers]
  # return sum(x ** 2 for x in numbers)
  # return sum(map(lambda x: x**2, numbers))
  res = 0
  for i in numbers:
    res += i**2
  return res

print(square_sum([1, 2]))