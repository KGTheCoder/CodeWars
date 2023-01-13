import math

def mygcd(x, y):
  # return x if y == 0 else mygcd(y, x % y)
  return math.gcd(x, y)


print(mygcd(30, 12))