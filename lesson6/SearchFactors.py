from TrieMap import TrieMap  # Import the class from TrieMap.py

class SuffixTrie(TrieMap):
  """ Suffix Trie implementation using TrieMap with factor-based approximate search """

  def __init__(self, text):
    """ Constructs a suffix trie from the given text (with a terminal $). """
    super().__init__([])
    self.text = text + "$"  # Store original text with special character
    for i in range(len(self.text)):
      self.add(self.text[i:], i)  # Add each suffix with its starting index

  def _get_leaves(self, node):
    """ Helper function to collect all positions stored in the subtree. """
    positions = []
    if 'value' in node:
      positions.append(node['value'])  # Store position
    for child in node:
      if child != 'value':
        positions.extend(self._get_leaves(node[child]))  # Recursion
    return sorted(positions)  # Return sorted list of positions

  def search_exact(self, query):
    """ Searches for exact matches of the query in the suffix trie. """
    node = self.root
    for c in query:
      if c not in node:
        return []
      node = node[c]
    return self._get_leaves(node)

  def search_with_factors(self, query):
    """ Searches for occurrences of query allowing up to 1 mismatch using factorization. """
    if len(query) < 2:
      return self.search_exact(query)  # Too short to split, do exact search
    
    mid = len(query) // 2
    left_part, right_part = query[:mid], query[mid:]
    
    left_positions = self.search_exact(left_part)
    right_positions = self.search_exact(right_part)
    
    results = []
    for left_pos in left_positions:
      full_pos = left_pos  # Position where left half starts
      if full_pos + len(query) <= len(self.text):
        segment = self.text[full_pos:full_pos + len(query)]
        mismatches = sum(1 for a, b in zip(segment, query) if a != b)
        if mismatches <= 1:
          results.append(full_pos)
    
    for right_pos in right_positions:
      full_pos = right_pos - mid  # Adjust to the start of the full query
      if full_pos >= 0 and full_pos + len(query) <= len(self.text):
        segment = self.text[full_pos:full_pos + len(query)]
        mismatches = sum(1 for a, b in zip(segment, query) if a != b)
        if mismatches <= 1 and full_pos not in results:
          results.append(full_pos)
    
    return sorted(results)

# Example Usage
if __name__ == "__main__":
  text = "bananabbb"
  suffix_trie = SuffixTrie(text)

  query = "ana"
  print(f"Occurrences of '{query}' with up to 1 mismatch:", suffix_trie.search_with_factors(query))