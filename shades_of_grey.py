def shades_of_grey(n):
  # return ['#{0:02x}{0:02x}{0:02x}'.format(i+1) for i in range(min(254, n))]

  """
  my_list = []
  if n <= 0:
    return []
  elif n > 254:
    n = 254

  for i in range(1, n+1):
    h_num = hex(i)[2:]
    if len(h_num) == 1:
      h_num = '0' + h_num
    h_num = '#' + h_num * 3
    my_list.append(h_num)

  return my_list
  """

  

print(shades_of_grey(200))