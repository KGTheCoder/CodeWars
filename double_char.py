def double_char(s):
  new_string = ""
  for i in s:
    new_string += i + i
  return new_string

print(double_char("String"))