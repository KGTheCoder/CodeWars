import string

def DNA_strand(dna):
  """
  pairs = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
  }
  return "".join([pairs[x] for x in dna])
  """

  # return dna.translate(string.maketrans("ATTGC","TAGC"))

  dnaComplement = ''
  for s in dna:
    if s == 'A':
      dnaComplement += 'T'
    elif s == 'T':
      dnaComplement += 'A'
    elif s == 'G':
      dnaComplement += 'C'
    elif s == 'C':
      dnaComplement += 'G'
  return dnaComplement

print(DNA_strand("ATTGC"))