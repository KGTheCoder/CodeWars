from math import isqrt

def is_square(arr):
  """
  for i in arr:
    return i == math.isqrt(i) ** 2
  """

  """
  if arr:
    return all((a ** 0.5).is_integer() for a in arr)
  """

  if arr:
    return all(isqrt(x)**2 == x for x in arr)

print(is_square([1, 4, 9, 16, 25, 36]))