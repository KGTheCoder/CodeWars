def high(x):
  """
  alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
  }
  for i in x:
    if i 
  """

  # return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

  """
  words = x.split(' ')
  l = []
  for i in words:
    scores = [sum([ord(char) - 96 for char in i])]
    print(i, scores)
    l.append(scores)
  print(l)
  return words[l.index(max(l))]
  """

  """
  maxValue = 0
  maxWord = ""

  values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
  
  words = x.split()

  print("words:", words)

  for word in words:
    currentSum = 0
    for char in word:
      currentSum += values[char]
      
      print("currentSum = ", currentSum)
    
    if currentSum > maxValue:
      maxValue = currentSum
      maxWord = word
  
  return maxWord
  """

  

print(high("man i need a taxi up to ubud"))