
def is_valid_IP(string):
  """
  parts = string.split(".")
  if len(parts) != 4:
    return False
  for item in parts:
    if not item.isdigit():
      return False
    if len(item) > 1 and item[0] == '0':
      return False
    i = int(item)
    if i < 0 or i > 255:
      return False
  return True
  """

  if string.count('.') != 3: return False
  try:
    tmp = list(str(n) for n in map(int, string.split(".")) if 0 <= n <= 255)
    print(tmp)
  except:
    return False
  return string == '.'.join(tmp)


print(is_valid_IP("1.2.3.4"))