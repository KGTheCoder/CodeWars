def divisible_by_three(n):
  n2 = 0
  for i in n:
    n2 += int(i)
  if n2 % 3 == 0:
    return True
  return False


print(divisible_by_three('123'))