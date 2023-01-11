def final_grade(exam, projects):
  """
  final_grade = 0
  if exam > 90 and projects > 10:
    final_grade = 100
  elif exam > 75 and projects >= 5:
    final_grade = 90
  elif exam > 50 and projects >= 2:
    final_grade = 75
  return final_grade
  """

  if exam > 90 or projects > 10: return 100
  if exam > 75 and projects >= 5: return 90
  if exam > 50 and projects >= 2: return 75
  return 0

n
print(final_grade(100, 12))