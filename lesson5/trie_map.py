class TrieMap(object):
    """ Trie implementation of a map.  Associating keys (strings or other
        sequence type) with values.  Values can be any type. """
    
    def __init__(self, kvs):
        self.root = {}
        # For each key (string)/value pair
        for (k, v) in kvs: self.add(k, v)
    
    def add(self, k, v):
        """ Add a key-value pair """
        cur = self.root
        for c in k: # for each character in the string
            if c not in cur:
                cur[c] = {} # if not there, make new edge on character c
            cur = cur[c]
        cur['value'] = v # at the end of the path, add the value
    
    def query(self, k):
        """ Given key, return associated value or None """
        cur = self.root
        for c in k:
            if c not in cur:
                return None # key wasn't in the trie
            cur = cur[c]
        # get value, or None if there's no value associated with this node
        return cur.get('value')
    
mp = TrieMap([("hello", "value 1"), ("there", 2), ("the", "value 3")])
print(mp.query("hello"))
print(mp.query("there"))
print(mp.query("NonExisting"))