def get_grade(s1, s2, s3):
  avg = (s1 + s2 + s3) / 3
  if avg >= 90 and avg <= 100:
    return 'A'
  elif avg >= 80 and avg < 90:
    return 'B'
  elif avg >= 70 and avg < 80:
    return 'C'
  elif avg >= 60 and avg < 70:
    return 'D'
  return 'F'

print(get_grade(95, 90, 93))