def reverse_words(text):
  """
  new_text = text.split()
  rev_text = ""
  for i in new_text:
    rev_text = rev_text + " " + i[::-1]
  return rev_text.lstrip()
  """
  """
  return ' '.join(s[::-1] for s in text.split(' '))
  """
  new_text = []
  for i in text.split(' '):
    new_text.append(i[::-1])
  return ' '.join(new_text)


print(reverse_words("The quick brown fox jumps over the lazy dog"))