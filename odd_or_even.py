def odd_or_even(arr):
  """
  for i in arr:
    if i == 0:
      return "even"
    else:
      return ("even" if sum(arr == 0))
  """

  # return 'even' if sum(arr) % 2 == 0 else 'odd'

  if sum(arr) % 2 == 0:
    return 'even'
  else:
    return 'odd'

print(odd_or_even([0, 1, 2, 3, 4, 5]))