def divisible_by_three(st):
  '''
  n2 = 0
  for i in n:
    n2 += int(i)
  if n2 % 3 == 0:
    return True
  return False
  '''

  while len(st) != 1:
    st = str(sum(int(n) for n in st))
  return int(st) in [0, 3, 6, 9]


print(divisible_by_three('123'))