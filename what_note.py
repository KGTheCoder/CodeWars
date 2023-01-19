def what_note(string, fret):
  """
  notes = "A, A#, B, C, D, D#, E, F, F#, G, G#".split(', ')
  return notes[(notes.index(string.upper()) + fret)%len(notes)]
  """
  
  E = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']

print(what_note("e", 0))