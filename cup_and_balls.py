def cup_and_balls(b, arr):
  """
  for i in range(len(arr)):
    print(arr[i])
  """

  """
  for switch in arr:
    print("switch =", switch)
    if b in switch:
      b = sum(switch) - b
  return b
  """

  for l, r in arr:
    b = r if b == l else l if b == r else b
  return b


print(cup_and_balls(1, [[2, 3], [1, 2], [1, 2]]))