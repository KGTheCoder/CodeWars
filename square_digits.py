def square_digits(num):
  """
  for n in str(num):
    num += n**2
  """

  """
  res = ""
  for n in str(num):
    res += str(int(n)**2)
  return int(res)
  """

  # return int(''.join(str(int(n)**2) for n in str(num)))

  num = str(num)
  ans = ''
  for n in num:
    ans += str(int(n)**2)
  return ans

print(square_digits(9119))