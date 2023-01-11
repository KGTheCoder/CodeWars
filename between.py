def between(a, b):
  # return list(range(a, b+1))

  # return [result for result in range(a, b+1)]

  arr = []
  for i in range(a, b + 1):
    arr.append(i)
  return arr

print(between(1, 4))