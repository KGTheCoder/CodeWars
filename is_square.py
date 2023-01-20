import math

def is_square(arr):
  """
  for i in arr:
    return i == math.isqrt(i) ** 2
  """

  if arr:
    return all((a ** 0.5).is_integer() for a in arr)


print(is_square([1, 4, 9, 16, 25, 36]))