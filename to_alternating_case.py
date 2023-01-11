def to_alternating_case(string):
 # return string.swapcase()

 # return ''.join([c.upper() if c.lower() else c.lower() for c in string])

  strn = ""
  for i in string:
    if i.isupper():
      strn += i.lower()
    else:
      strn += i.upper()
  return strn


print(to_alternating_case("hello world"))