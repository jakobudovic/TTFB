from TrieMap import TrieMap  # Import the class from TrieMap.py

class SuffixTrie(TrieMap):
  """ Suffix Trie implementation using TrieMap with approximate search """

  def __init__(self, text):
    """ Constructs a suffix trie from the given text (with a terminal $). """
    super().__init__([])
    text += "$"  # Add special character to mark the end
    for i in range(len(text)):
      self.add(text[i:], i)  # Add each suffix with its starting index

  def _get_leaves(self, node):
    """ Helper function to collect all positions stored in the subtree. """
    positions = []
    if 'value' in node:
      positions.append(node['value'])  # Store position
    for child in node:
      if child != 'value':
        positions.extend(self._get_leaves(node[child]))  # Recursion
    return sorted(positions)  # Return sorted list of positions

  def _search_with_mismatches(self, node, query, index, mismatches, max_mismatches):
    """ Recursively search for query with up to max_mismatches. """
    if index == len(query):
      return self._get_leaves(node)
    
    results = []
    for char in node:
      if char == 'value':
        continue
      
      new_mismatches = mismatches + (1 if char != query[index] else 0)
      if new_mismatches <= max_mismatches:
        results.extend(self._search_with_mismatches(node[char], query, index + 1, new_mismatches, max_mismatches))
    
    return results
  
  def search_with_mismatches(self, query, max_mismatches=2):
    """ Search for occurrences of query with up to max_mismatches allowed. """
    return self._search_with_mismatches(self.root, query, 0, 0, max_mismatches)

# Example Usage
if __name__ == "__main__":
  #       01234567890123
  text = "banananenebbbb"
  suffix_trie = SuffixTrie(text)

  query = "ana"
  print(f"Occurrences of '{query}' with up to 2 mismatches:", suffix_trie.search_with_mismatches(query, 2))
