def rental_car_cost(d):
  """
  total = 40
  days = 0
  if d >= 3:
    total - 20
  return total
  """

  """
  result = d * 40
  if d >= 7:
    result -= 50
  elif d >= 3:
    result -= 20
  return result
  """

  return d * 40 - (d > 2) * 20 - (d > 6) * 30

print(rental_car_cost(3))