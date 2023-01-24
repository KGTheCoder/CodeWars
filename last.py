def last(s):
  """
  res = s.split()
  return sorted(res, key=lambda x: int(x[-1]))
  """

  # return sorted(s.split(), key=lambda x: x[-1])

  a = s.split()
  last_char = []
  i = 0
  for word in a:
    last_char.append((word[-1], i, word))
    i = i + 1
  last_char = sorted(last_char)
  output = [word for char, i, word in last_char]
  return output

print(last("man i need a taxi up to ubud"))