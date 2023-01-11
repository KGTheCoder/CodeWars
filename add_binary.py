def add_binary(a, b):
  # return bin(a+b)[2:]
  return format(a + b, 'b')

print(add_binary(1, 1))