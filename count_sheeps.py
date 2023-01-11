def count_sheeps(sheep):
  """
  count = 0
  for i in sheep:
    if i == True:
      count += 1
  return count
  """

 # return sheep.count(True)

  return len([x for x in sheep if x])

print(count_sheeps([
  True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True
]))