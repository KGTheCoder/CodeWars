def find_uniq(arr):
  """
  unique = arr[0]
  for i in arr:
    if i != unique:
      print(i)
      return arr[i]
  """

  a, b = set(arr)
  return a if arr.count(a) == 1 else b


print(find_uniq([2, 1, 1, 1, 1, 1]))