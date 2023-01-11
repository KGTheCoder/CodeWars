def high_and_low(numbers):
  """
  nums = [int(n) for n in numbers.split()]
  max_num = str(max(nums))
  min_num = str(min(nums))
  return max_num, min_num
  """

  """
  nn = [int(s) for s in numbers.split()]
  return "%d %d" % (max(nn), min(nn))
  """

  """
  numlist = numbers.split(" ")
  print(numlist)
  i = 0

  highest = int(numlist[0])
  lowest = int(numlist[0])

  while i < len(numlist):
    numlist[i] = int(numlist[i])
    if numlist[i] > highest:
      highest = numlist[i]
    if numlist[i] < lowest:
      lowest = numlist[i]
    i += 1

  highest = str(highest)
  lowest = str(lowest)
  return highest + " " + lowest
  """

  """
  nums = [int(x) for x in numbers.split(" ")]
  return f"{max(nums)} {min(nums)}"
  """

  a = list(map(int, numbers.split()))
  return f"{max(a)} {min(a)}"

print(high_and_low("1 2 3 4 5"))