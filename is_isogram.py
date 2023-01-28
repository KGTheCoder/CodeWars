def is_isogram(string):
  """
  chars = 'abcdefghijklmnopqrstuvwxyz'
  for char in chars:
    count = string.lower().count(char)
    if count > 1:
      return False
  return True
  """

  # return len(string) == len(set(string.lower()))

  string = string.lower()
  for letter in string:
    if string.count(letter) > 1: return False
  return True


print(is_isogram('moseo'))