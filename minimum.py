def minimum(a, x):
  return min(a % x, -a % x)

print(minimum([10, 6]))