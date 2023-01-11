"""
def two_sort(array):
  new_array = sorted(array)
  for i in new_array[0]:
    print(i,"***",end="")
  

print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))
"""

"""
def two_sort(array):
  return '***'.join(min(array))
"""

def two_sort(array):
  return '***'.join(sorted(array)[0])

print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))