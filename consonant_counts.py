def consonant_count(s):
  """
  consonants = "AaEeIiOoUu"
  res = 0
  for i in s:
    if i not in consonants and i.isalpha():
      res += 1
  return res
  """

  return sum(1 for c in s if c.isalpha() and c.lower() not in "aeiou")

print(consonant_count("aaaaab"))