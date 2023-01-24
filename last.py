def last(s):
  """
  res = s.split()
  return sorted(res, key=lambda x: int(x[-1]))
  """

  return sorted(s.split(), key=lambda x: x[-1])

print(last("man i need a taxi up to ubud"))