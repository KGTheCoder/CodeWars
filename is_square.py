import math

def is_square(n):
  """
  root = math.sqrt(n)
  if (root + 0.5) ** 2 == n:
    return True
  else:
    return False
  """

  return n > -1 and math.sqrt(n) % 1 == 0


print(is_square(-1))