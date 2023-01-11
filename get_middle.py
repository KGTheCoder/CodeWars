def get_middle(s):
  """
  for i in s:
    if len(s) % 2 == 0:
      return 
  """

  """
  y = int(len(s)/2)
  if len(s) % 2 == 0:
    return s[y-1:y+1]
  else:
    return s[y:y+1]
  """

  a = len(s)
  if len(s) == 1:
    return s
  elif len(s) % 2 == 0:
    return s[int(a/2) -1] + s[int(a/2)]
  else:
    return s[int(a/2)]


print(get_middle("test"))