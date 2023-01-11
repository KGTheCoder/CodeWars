def square_digits(num):
  """
  for i in map(str, num):
    i += i
  return num
  """

  """
  res = ""
  for x in str(num):
    res += str(int(x)**2)
  return int(res)
  """

  # return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9119))