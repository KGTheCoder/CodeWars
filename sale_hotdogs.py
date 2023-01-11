def sale_hotdogs(n):
  """
  if n < 5:
    return 100
  elif n >= 5 and n < 10:
    return 95
  elif n >= 10:
    return 90
  return 0
  """

  # return n * (100 if n < 5 else 95 if n < 10 else 90)

  if n < 5:
    return n * 100
  elif n >= 10:
    return n * 90
  else:
    return n * 95

print(sale_hotdogs(5))