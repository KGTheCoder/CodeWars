def unique_in_order(iterable):
  myset = set(iterable)
  return list(myset)

print(unique_in_order([1, 2, 2, 3, 3]))