def get_count(sentence):
  vowels = "aeiou"
  count = 0
  for v in sentence:
    if v in vowels:
      count += 1
  return count


print(get_count("aeiou"))