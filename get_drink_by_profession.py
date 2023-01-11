"""
def get_drink_by_profession(param):
  dic = {
    "Jabroni": "Patron Tequila",
    "School Counselor": "Anything with Alcohol",
    "Programmer": "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine",
    "Politician": "Your tax dollars",
    "Rapper": "Cristal"
  }
  for k, v in dic.items():
    if k == param:
"""


dic = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
  }
def get_drink_by_profession(param):
  return dic.get(param.lower(), "Beer")


print(get_drink_by_profession("jabr0ni"))