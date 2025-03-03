from TrieMap import TrieMap  # Import the class from TrieMap.py

class SuffixTrie(TrieMap):
  """ Suffix Trie implementation using TrieMap """

  def __init__(self, text):
    """ Constructs a suffix trie from the given text (with a terminal $). """
    super().__init__([])  # Initialize an empty TrieMap
    text += "$"  # Add special character to mark the end
    for i in range(len(text)):
      self.add(text[i:], i)  # Add each suffix with its starting index

  def is_substring(self, query):
    """ Checks if a given query is a substring of the original text. """
    node = self.root
    for c in query:
      if c not in node:
        return False
      node = node[c]
    return True

  def _get_leaves(self, node):
    """ Helper function to collect all positions stored in the subtree. """
    positions = []
    if 'value' in node:
      positions.append(node['value']) # Store position
    for child in node:
      if child != 'value':
        positions.extend(self._get_leaves(node[child])) # Recursion
    return sorted(positions) # Return sorted list of positions
  
  def get_occurrences(self, query):
    """ Returns the occurrences of a query in the suffix trie. """
    node = self.root
    for c in query:
      if c not in node:
        return [] # Query is not a substring
      node = node[c]
    return self._get_leaves(node)
  
  def count_occurrences(self, query):
    return len(self.get_occurrences(query))

# Example Usage
if __name__ == "__main__":
  text = "banana"
  suffix_trie = SuffixTrie(text)

  queries = ["ana", "ban", "nana", "apple"]
  for q in queries:
    print(f"'{q}' is substring:", suffix_trie.is_substring(q))
    print(f"Occurrences of '{q}':", suffix_trie.count_occurrences(q))
    print(f"Occurrences of '{q}':", suffix_trie.get_occurrences(q))
