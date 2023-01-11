from collections import Counter

def count(string):
  """
  counter = {}
  for i in string:
    counter[i] = string.count(i)
  return counter
  """

  # return Counter(string)

  return {i: string.count(i) for i in string}


print(count("aba"))