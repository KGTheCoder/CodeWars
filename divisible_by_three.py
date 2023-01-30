def divisible_by_three(st):
  '''
  n2 = 0
  for i in n:
    n2 += int(i)
  if n2 % 3 == 0:
    return True
  return False
  '''

  '''
  while len(st) != 1:
    st = str(sum(int(n) for n in st))
    print(st)
  return int(st) in [0, 3, 6, 9]
  '''

  if len(st) == 1:
    return st in '369'
  return divisible_by_three(str(sum(map(int, st))))
print(divisible_by_three('19254'))