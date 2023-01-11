def wave(word):
  """
  if str == []:
    return []
  else:
    res = []
    for i in range(len(list(word))):
      if word[i] != " ":
        word_update = list(''.join(word).lower())

        print("word_update =", word_update, "\n")

        word_update[i] = word_update[i].upper()

        print("word_update[i] =", word_update[i])

        res.append(''.join(word_update))
  return res
  """

  return [word[:i] + word[i].upper() + word[i+1:] for i in range(len(word)) if word[i].isalpha()]


print(wave("hello"))