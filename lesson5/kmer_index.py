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

def search_in_index(reference, kmer_hash, k, sequence):
  """Search all k-mers from the input sequence and verify exact matches."""
  if len(sequence) < k:
    print("Input sequence is shorter than k-mer size.")
    return []

  occurrences = []
  for i in range(len(sequence) - k + 1):
    # Find where this k-mer appears
    kmer = sequence[i:i+k]
    candidate_positions = kmer_hash.get(kmer,[])
    print("For k-mer '%s' found %d candidate positions" % (kmer,len(candidate_positions)))
    # Verify exact-match of the sequence at each found position in the reference
    for pos in candidate_positions:
      if reference[pos-i:pos-i+len(sequence)] == sequence:
        occurrences.append(pos - i)

  return list(set(occurrences)) # Remove duplicates

def search_sequence(reference, kmer_hash, k, sequence):
  start_time = time.time()
  occ = search_in_index(reference,kmer_hash,k,sequence)
  end_time = time.time()
  # Print Results
  print("Found %d exact matches in %2.3f s." % (len(occ),end_time-start_time))
  for pos in occ: 
    print("%d " % pos,end="")

if __name__ == "__main__":
  # Arguments Parser
  parser = argparse.ArgumentParser(
    description="Index a FASTA using a hash and exact search an input sequence")
  parser.add_argument("-r","--reference",help="Path to the FASTA file",required=True)
  parser.add_argument("-i","--input-seq",help="Input Sequence",required=True)
  parser.add_argument("-k","--kmer-len",help="K-mer length",default=6)
  args = parser.parse_args()
  sequence = args.input_seq
  k = int(args.kmer_len)
  # Read FASTA file
  print("Reading input FASTA ...",end="")
  reference = read_fasta(args.reference)
  print(" read %d bases from '%s'." % (len(reference),args.reference))
  # Build hash table
  print("Building hash table ...")
  kmer_hash = build_kmer_index(reference,k)
  # Search sequence
  print("Searching '%s' sequence ..." % sequence)
  search_sequence(reference,kmer_hash,k,sequence)
  