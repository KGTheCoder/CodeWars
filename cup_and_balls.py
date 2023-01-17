def cup_and_balls(b, arr):
  """
  for i in range(len(arr)):
    print(arr[i])
  """

  for switch in arr:
    if b in switch:
      b = sum(switch) - b
  return b

print(cup_and_balls(2, [[1, 2]]))