def create_phone_number(n):
  # return "({}{}{}) {}{}{}-{}{}{}".format(*n)

  """
  n = "".join(map(str, n))
  return "(%s) %s-%s"%(n[:3], n[3:6], n[6:])
  """

  # return "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])

  res = '({}{}{}) {}{}{}-{}{}{}{}'.format(n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9])
  return res

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))