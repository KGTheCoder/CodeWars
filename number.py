def number(lines):
  """
  if not lines:
    return []
  else:
    for i in lines:
      dic = dict(zip(i, lines))
    return dic
  """

  """
  x = 1
  for i in range(len(lines)):
    lines[i] = str(x) + ": " + lines[i]
    x +=1 
  return lines
  """

  # return ['%d: %s' % v for v in enumerate(lines, 1)]

  return [f"{counter}: {line}" for counter, line in enumerate(lines, 1)]




print(number(["a", "b", "c"]))