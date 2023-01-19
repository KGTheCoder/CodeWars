def minimum(a, x):
  # return min(a % x, -a % x)
  # return abs(a-round(a/x)*x)
  near = x
  while near < a:
    near += x
  plus = near - a
  minus = a-(near-x)
  return plus if plus < minus else minus 

print(minimum(10, 6))