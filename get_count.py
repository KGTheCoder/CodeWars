def get_count(sentence):
  """
  vowels = "aeiou"
  count = 0
  for v in sentence:
    if v in vowels:
      count += 1
  return count
  """

 # return sum(1 for v in sentence if v in "aeiouAEIOU")

  return sum(v in "aeiou" for v in sentence)


print(get_count("aeiou"))