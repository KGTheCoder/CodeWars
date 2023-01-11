"""
def sum_mix(arr):
  new_arr = [int(x) for x in arr]
  return sum(new_arr)
"""

def sum_mix(arr):
  return sum(map(int, arr))

print(sum_mix([9, 3, '7', '3']))