def format_money(amount):
  # print("$",amount)
  return '${:.2f}'.format(amount)

format_money2 = lambda x: '${:.2f}'.format(x)

print(format_money(3))