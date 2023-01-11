def count_sheep(n):
  """
  for i in len(n+1):
    return f"{n} sheep..."
  """

  """
  sheep = ""
  for i in range(1, n+1):
    sheep += str(i) + " sheep..."
  return sheep
  """

  return ''.join(f"{i} sheep... " for i in range(1, n+1))

print(count_sheep(3))