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

  print(res)