def reverse_number(n):
  """
  str(n)
  return str(n[::-1])
  """

  """
  if n < 0: return -reverse_number(-n)
  return int(str(n)[::-1])
  """

  """
  if n >= 0:
    return int(str(n)[::-1])
  else:
    return -int(str(n)[:0:-1])
  """

  

print(reverse_number(-123))