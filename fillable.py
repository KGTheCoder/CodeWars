"""
def fillable(stock, merch, n):
  for k, v in stock.items():
    if k == merch and v == n or v >= n:
      return True
    else:
      return False
"""


def fillable(stock, merch, n):
  return stock.get(merch, 0) >= n

stock = {
  'football': 4,
  'boardgame': 10,
  'leggos': 1,
  'doll': 5
}

print(fillable(stock, 'football', 3))
print(fillable(stock, 'leggos', 2))
print(fillable(stock, 'pizza', 5))
