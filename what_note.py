def what_note(string, fret):
  notes = "A, A#, B, C, D, D#, E, F, F#, G, G#".split(', ')
  return notes[(notes.index(string.upper()) + fret)%len(notes)]

print(what_note("e", 0))