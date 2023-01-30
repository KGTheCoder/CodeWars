def sort_by_value_and_index(arr):
  '''
  res = []
  for x in arr:
  '''

  return [b for _, b in sorted(enumerate(arr, 1), key=lambda a: a[0] * a[1])]




print(sort_by_value_and_index([23, 2, 3, 4, 5]))