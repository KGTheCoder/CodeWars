def seven_ate9(s):
  """
  while s.find('797') != -1:
    s = s.replace('797', '77')
  return s
  """

  while '797' in s:
    s = s.replace('797', '77')
  return s


print(seven_ate9('79712312'))