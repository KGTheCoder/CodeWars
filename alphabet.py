def alphabet(ns):
  ns = sorted(ns)
  print(ns)
  ns.remove(ns[0] * ns[1])
  print(ns)
  return ns[-1] / ns[2]

print(alphabet([2, 3, 4, 1, 12, 6, 2, 4]))