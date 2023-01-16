def my_languages(results):
  """
  for k, v in results.items():
    print(k, v)
  """

  # return sorted((l for l, r in results.items() if r >= 60), reverse = True, key = results.get)

  array_list = []
  sorted_results = (sorted(results.items(), key = lambda k: k[1], reverse = True))
  print("sorted_results =", sorted_results)
  for i in sorted_results:
    if i[1] >= 60:
      array_list.append(i[0])
  return array_list


print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))