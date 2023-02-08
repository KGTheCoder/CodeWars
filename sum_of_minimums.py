def sum_of_minimums(numbers):
  '''
  min_num = 0
  for i in numbers:
    for j in numbers:
      print(min_num)
      min_num += min(j)

    return min_num
  '''

  total = 0
  for nums in numbers:
    total += min(nums)
  return total 


print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))

