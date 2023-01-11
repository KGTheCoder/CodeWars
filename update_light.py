def update_light(current):
  """
  if current == 'green':
    current = 'yellow'
  elif current == 'yellow':
    current = 'red'
  elif current == 'red':
    current = 'green'
  return current
  """

  return {"green": "yellow", "yellow": "red", "red": "green"}[current]

print(update_light('green'))