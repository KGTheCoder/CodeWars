import math

def grow(arr):
  """
  for i in arr:
    for j in arr:
      return i * j
  """

  """
  res = 1
  for i in arr:
    res = res * i
  return res
  """

  return math.prod(arr)

print(grow([1, 2, 3, 4]))