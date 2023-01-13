def number(bus_stops):
  """
  initial = bus_stops[0][0]
  for i in range(len(bus_stops)):
    initial += bus_stops[i][0]
    return initial
  """

  # return sum([stop[0] - stop[1] for stop in bus_stops])

  people_in = 0
  people_out = 0
  for stops in bus_stops:
    people_in += stops[0]
    people_out += stops[1]
  return people_in - people_out

print(number([[10, 0], [3, 5], [5, 8]]))