def xo(s):
  """
  x_count = 0
  o_count = 0
  for char in s:
    if 'x' or 'o' not in s:
      return False
    elif 'x' in s:
      x_count += 1
    elif 'o' in s:
      o_count += 1
  return x_count == o_count
  """

  """
  s = s.lower()
  return s.count('x') == s.count('o')
  """

  exes = 0
  ohs = 0

  for c in s.lower():
    if c == 'x':
      exes += 1
    elif c == 'o':
      ohs += 1
  
  return exes == ohs


print(xo('xo'))