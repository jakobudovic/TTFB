def hamming_distance(seq1, seq2):
  """Compute the Hamming distance between two sequences of equal length."""
  if len(seq1) != len(seq2):
    raise ValueError("Sequences must be of the same length")
  distance = 0
  for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
      distance += 1
  return distance

def hamming_alignment(seq1, seq2):
  """Generate a list of 'M' (match) and 'X' (mismatch) based on Hamming distance."""
  if len(seq1) != len(seq2):
    raise ValueError("Sequences must be of the same length")
  alignment = []
  for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
      alignment.append('M')
    else:
      alignment.append('X')
  return alignment

def pretty_print_alignment(seq1, seq2, alignment):
  """Pretty prints the alignment of two sequences with match markers."""
  if len(seq1) != len(seq2) or len(seq1) != len(alignment):
    raise ValueError("Sequences and alignment must have the same length")

  match_line = ''.join('|' if symbol == 'M' else ' ' for symbol in alignment)

  print(seq1)
  print(match_line)
  print(seq2)


seq1 = "ACGTGCA"
seq2 = "ATGAGGA"

distance = hamming_distance(seq1, seq2)
print(distance)  # Output: 3
alignment = hamming_alignment(seq1, seq2)
print(alignment)  # Output: ['M', 'X', 'M', 'X', 'M', 'X', 'M']
# Pretty print
# ACGTGCA
# | | | |
# ATGAGGA
pretty_print_alignment(seq1, seq2, alignment)







