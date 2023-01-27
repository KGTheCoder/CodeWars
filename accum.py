def accum(s):
  # return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
  i = 0
  result = ''
  for letter in s:
    result += letter.upper() + letter.lower() * i + '-'
    i += 1
  return result[:len(result)-1]


print(accum('abcd'))