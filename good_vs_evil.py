def good_vs_evil(good, evil):
  """
  good_side = {
    "Hobbits": 1,
    "Men": 2,
    "Elves": 3,
    "Dwarves": 3,
    "Eagles": 4,
    "Wizards": 10
  }

  evil_side = {
    "Orcs": 1,
    "Men": 2,
    "Wargs": 2,
    "Goblins": 2,
    "Uruk Hai": 3,
    "Trolls": 5,
    "Wizards": 10
  }
  worth = 0
  test = "".join(map(good_side, good))
  return test
  """

  points_good = [1, 2, 3, 3, 4, 10]
  points_evil = [1, 2, 2, 2, 3, 5, 10]

  good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
  evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

  result = "Battle Result: "

  if good < evil:
    return result + "Evil eradicates all trace of Good."
  elif good > evil:
    return result + "Good triumphs over Evil."
  else:
    return result + "No victor on this battle field."


print(good_vs_evil("1 1 1 1 1 1", "1 1 1 1 1 1 1"))