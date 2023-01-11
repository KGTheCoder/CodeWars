"""
def invert(lst):
  new_lst = []
  for i in lst:
    i *= -1
    new_lst += i
  return new_lst
"""

"""
def invert(lst):
  return [-x for x in lst]
"""

"""
def invert(lst):
  return list(map(lambda x: -x, lst))
"""

# print(invert([1, 2, 3, 4, 5]))