def my_languages(results):
  """
  for k, v in results.items():
    if v >= 65:
      return v
  """

  return sorted((l for l, r in results.items() if r>= 60), reverse = True, key = results.get)

print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))