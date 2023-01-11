"""
def minimum(arr):
  min = arr[0]
  for i in arr:
    if i < min:
      min = i
  return min

def maximum(arr):
  max = arr[0]
  for i in arr:
    if i > max:
      max = i
  return max
"""

def minimum(arr):
  return min(arr)

def maximum(arr):
  return max(arr)
  
print(minimum([4, 6, 2, 1, 9, 63, -234, 566]))
print(maximum([4, 6, 2, 1, 9, 63, -234, 566]))