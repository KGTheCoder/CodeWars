def disemvowel(text):
  """
  for i in "aeiouAEIOU":
    text = text.replace(i, "")
  return text
  """

  # return "".join(c for c in text if c.lower() not in "aeiou")

  vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
  res = ""
  for i in text:
    if not i in vowels:
      res += i
  return res


print(disemvowel("This website is for losers LOL!"))