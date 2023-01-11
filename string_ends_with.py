def solution(string, ending):
  """
  if ending in string[-2:]:
    return True
  return False
  """
  return string.endswith(ending)


print(solution('abc', 'bc'))