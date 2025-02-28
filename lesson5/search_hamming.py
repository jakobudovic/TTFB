import argparse
import time

def read_fasta(file_path):
  """Read a FASTA file and return a string with all the content"""
  sequence = []
  with open(file_path, 'r') as file:
    for line in file:
      if not line.startswith('>'):
        sequence.append(line.strip())  # Remove newline and concatenate
  return ''.join(sequence)

def build_kmer_index(sequence, k):
  """Create a hash table of k-mers and their positions."""
  kmer_index = {}
  for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    if kmer in kmer_index:
      kmer_index[kmer].append(i)
    else:
      kmer_index[kmer] = [i]
  return kmer_index

def hamming_distance(seq1, seq2):
  """Compute the Hamming distance between two sequences of equal length."""
  if len(seq1) != len(seq2):
    raise ValueError("Sequences must be of the same length")
  distance = 0
  for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
      distance += 1
  return distance

def search_sequence(reference, sequence, m):
  start_time = time.time()
  matches = []
  for i in range(0,len(reference)-len(sequence)):
    if hamming_distance(reference[i:i+len(sequence)],sequence) <= m:
      matches.append(i)
  end_time = time.time()
  # Print Results
  print("Found %d exact matches in %2.3f s." % (len(matches),end_time-start_time))
  for match in matches: 
    print("%d " % match,end="")

if __name__ == "__main__":
  # Arguments Parser
  parser = argparse.ArgumentParser(
    description="Index a FASTA using a hash and exact search an input sequence")
  parser.add_argument("-r","--reference",help="Path to the FASTA file",required=True)
  parser.add_argument("-i","--input-seq",help="Input Sequence",required=True)
  parser.add_argument("-m","--mismatches",help="Maximum Mismatches",default=2)
  args = parser.parse_args()
  sequence = args.input_seq
  m = int(args.mismatches)
  # Read FASTA file
  print("Reading input FASTA ...",end="")
  reference = read_fasta(args.reference)
  print(" read %d bases from '%s'." % (len(reference),args.reference))
  # Search sequence
  print("Searching '%s' sequence ..." % sequence)
  search_sequence(reference,sequence,m)
  