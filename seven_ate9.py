# def seven_ate9(s):
"""
  while s.find('797') != -1:
    s = s.replace('797', '77')
  return s
"""
  
"""
  while '797' in s:
    s = s.replace('797', '77')
  return s
"""

# seven_ate9 = lambda s:''.join(x for i, x in enumerate(s) if s[i-1:i+2] != '797')

def seven_ate9(s):
  """
  i = 0
  n = len(s)
  new = ''
  while i < n:
    if s[i:i + 3] == '797':
      new += '7'
      i += 2
    else:
      new += s[i]
      i += 1
  return new
  """

  li = list(s)

  for idx, ele in enumerate(li):
    try:
      if li[idx - 1] == '7' and li[idx + 1] == '7' and li[idx] == '9':
        li.pop(idx)
    except:
      print("IndexError: List Index Out of Range")
  
  return ''.join(li)


print(seven_ate9('79712312'))