def calculate_years(principal, interest, tax, desired):
  years = 0

  while principal < desired:
    principal += (interest * principal) * (1 - tax)
    years += 1

  return years

print(calculate_years(1000, 0.05, 0.18, 1100))