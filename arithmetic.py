def arithmetic(a, b, operator):
  """
  if operator == "add":
    return a + b
  elif operator == "subtract":
    return a - b
  elif operator == "multiply":
    return a * b
  elif operator == "divide":
    return a / b
  """

  return {
    'add': a + b,
    'subtract': a - b,
    'multiply': a * b,
    'divide': a / b,
  }[operator]

print(arithmetic(1, 2, "add"))