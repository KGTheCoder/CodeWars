def find_short(s):
  l = s.split()
  return len(min(l, key=len))


print(find_short('turns out random test cases are easier than writing out basic ones'))