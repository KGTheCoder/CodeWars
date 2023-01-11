def filter_list(l):
  """
  return [e for e in l if isinstance(e, int)]
  """
  """
  return [i for i in l if not isinstance(i, str)]
  """
  new_list = []
  for x in l:
    if type(x) != str:
      new_list.append(x)
  return new_list

print(filter_list([1, 2, 'a', 'b']))