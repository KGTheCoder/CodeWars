def only_one(*args):
  return sum(args) == 1
  

print(only_one(True, False))