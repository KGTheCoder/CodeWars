def count_correct_characters(correct, guess):
  """
  count = 0
  char_list = [correct, guess]
  for i in correct, guess:
    print(i if i in char_list)
  """

  if len(correct) != len(guess): raise Exception('Error')
  return sum(1 for i, j in zip(correct, guess) if i==j)

print(count_correct_characters("dog", "god"))