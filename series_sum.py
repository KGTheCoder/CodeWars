def series_sum(n):
  """
  res = 0
  series = (1 + (1/n+3))
  """

  res = 0.0
  for i in range(n):
    print("i =", i)
    res += 1 / (1 + i * 3)
    print(res)
  return round(res, 2)

print(series_sum(3))