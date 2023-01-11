def camel_case(string):
  # return string.title().replace(" ", "")

  return ''.join([i.capitalize() for i in string.split()])

print(camel_case("test case"))