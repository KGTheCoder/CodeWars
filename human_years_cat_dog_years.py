def human_years_cat_dog_years(human_years):
  """
  cat_years = 0
  dog_years = 0

  if human_years == 1:
    cat_years += 15
    dog_years += 15
  elif human_years == 2:
    cat_years += 24
    dog_years += 24
  elif human_years > 2:
    cat_years += 28
    dog_years += 24
  """

  cat_years = 0
  dog_years = 0
  if human_years == 1:
    cat_years += 15
    dog_years += 15
    return [human_years, cat_years, dog_years]
  elif human_years == 2:
    cat_years += 24
    dog_years += 24
    return [human_years, cat_years, dog_years]
  elif human_years > 2:
    cat_years += 24
    dog_years += 24
    years = human_years - 2
    cat_years += years * 4
    dog_years += years * 5
    return [human_years, cat_years, dog_years]

print(human_years_cat_dog_years(6))