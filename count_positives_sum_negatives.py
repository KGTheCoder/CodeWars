"""
def count_positives_sum_negatives(arr):
  pos_num = []
  neg_num = []
  pos_count = 0
  for i in arr:
    if i > 0:
      pos_num.append(i)
    else:
      neg_num.append(i)

  for i in pos_num:
    pos_count += 1

  neg_num_sum = sum(neg_num)
  res = []
  res.append(pos_count)
  res.append(neg_num_sum)

  if not arr:
    return []
    
  return res
"""

def count_positives_sum_negatives(arr):
  if not arr: return []
  pos = 0
  neg = 0
  for x in arr:
    if x > 0:
      pos += 1
    else:
      neg += x
  return [pos, neg]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))