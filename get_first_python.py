def get_first_python(users):
  """
  for data in users:
    if data['language'] == 'Python':
      return f'{data["first_name"]}, {data["country"]}'

  return 'There will be no Python developers'
  """

  return next(('{}, {}'.format(d['first_name'], d['country']) for d in users if d['language'] == 'Python'), 'There will be no Python developers')

list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

print(get_first_python(list1))