def find_short(s):
  '''
  l = s.split()
  return len(min(l, key=len))
  '''

  # return min(len(x) for x in s.split())

  sList = s.split()
  shortestLen = len(sList[0])
  for item in sList:
    if len(item) < shortestLen:
      shortestLen = len(item)
  return shortestLen


print(find_short('turns out random test cases are easier than writing out basic ones'))