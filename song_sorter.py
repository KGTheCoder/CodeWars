def song_sorter(lines):
  """
  real_lines = [
    "On the 12th day of Christmas my true love gave to me",
    "12 drummers drumming",
    "11 pipers piping", 
    "10 lords a leaping", 
    "9 ladies dancing", 
    "8 maids a milking",
    "7 swans a swimming", 
    "6 geese a laying", 
    "5 golden rings", 
    "4 calling birds",
    "3 French hens", 
    "2 turtle doves and", 
    "a partridge in a pear tree."
]

  return real_lines
"""

  return sorted(lines, key = lambda x: [
    'On', '12', '11', '10', '9', '8', '7', 
    '6', '5', '4', '3', '2', '1', 'and', 'a'
    ].index(x.split()[0]))

lines = [
  "On the 12th day of Christmas my true love gave to me",
  "11 pipers piping", 
  "9 ladies dancing", 
  "12 drummers drumming",
  "6 geese a laying", 
  "a partridge in a pear tree.",
  "5 golden rings", 
  "7 swans a swimming", 
  "4 calling birds",
  "3 French hens", 
  "10 lords a leaping", 
  "8 maids a milking",
  "2 turtle doves and", 
]
print(song_sorter(lines))