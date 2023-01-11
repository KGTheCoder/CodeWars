def disemvowel(string_):
  """
  for i in "aeiouAEIOU":
    string_ = string_.replace(i, "")
  return string_
  """
  return "".join(c for c in string_ if c.lower() not in "aeiou")

print(disemvowel("This website is for losers LOL!"))