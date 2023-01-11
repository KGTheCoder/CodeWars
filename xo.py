def xo(s):
  """
  count = 0
  for c in s:
    if not "x" or "o":
      return True
    elif "x" in s or "o" in s:
      count += 1
  if count % 2 == 0:
    print(count)
    return True
  else:
    print(count)
    return False
  """
  
  """
  s = s.lower()
  return s.count('x') == s.count('o')
  """

  return s.lower().count('x') == s.lower().count('o')


print(xo("xOxo"))