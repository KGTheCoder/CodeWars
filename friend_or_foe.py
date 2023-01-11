def friend(x):
  """
  new_x = []
  for i in x:
    if len(i) == 4:
      new_x.append(i)
  return new_x
  """
  return [f for f in x if len(f) == 4]

print(friend( ["Ryan", "Kieran", "Mark"]))