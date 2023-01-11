def get_age(age):
  # return int(age[0])
  for x in age:
    if x.isdigit():
      return int(x)

print(get_age("2 years old"))