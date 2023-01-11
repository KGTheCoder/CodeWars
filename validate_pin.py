import re

def validate_pin(pin):
  """
  if pin == 4:
    return True
  """
  # return len(pin) in (4, 6) and pin.isdigit()
  return bool(re.fullmatch("\d{4}|\d{6}", pin))

print(validate_pin("1234"))