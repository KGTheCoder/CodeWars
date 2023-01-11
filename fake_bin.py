def fake_bin(x):
  """
  new_x = int(x)
  res = 0
  for num in new_x:
    if num < 5:
      res += 0
    else:
      res += 1

  return res
  """

  # return ''.join('0' if c < '5' else '1' for c in x)

  result = ""
  for num in x:
    if int(num) < 5:
      result += "0"
    else:
      result += "1"

  return result

print(fake_bin("45385593107843568"))