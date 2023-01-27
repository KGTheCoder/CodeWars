def square_digits(num):
  """
  for n in str(num):
    num += n**2
  """

  res = ""
  for n in str(num):
    res += str(int(n)**2)
  return int(res)


print(square_digits(9119))