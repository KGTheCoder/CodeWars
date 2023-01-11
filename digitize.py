def digitize(n):
  """
  res = [int(x) for x in str(n)]
  res.reverse()
  return res
  """

  return [int(x) for x in str(n)[::-1]]

print(digitize(35231))