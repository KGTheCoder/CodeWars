def are_you_playing_banjo(name):
  """
  if name.startswith("R") or name.startswith("r"):
    return name + " plays banjo"
  else:
    return name + " does not play banjo"
  """

  if name[0].lower() == 'r':
    return name + ' plays banjo'
  else:
    return name + ' does not play banjo'

print(are_you_playing_banjo("Remy"))