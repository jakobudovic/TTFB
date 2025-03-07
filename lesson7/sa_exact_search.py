def build_suffix_array(text):
  suffixes = sorted((text[i:], i) for i in range(len(text)))
  return [idx for suffix, idx in suffixes]

def pattern_exists(text, pattern, sa):
  left, right = 0, len(sa) - 1
  while left <= right:
    mid = (left + right) // 2
    suffix = text[sa[mid]:]
    if suffix.startswith(pattern):
      return True
    elif pattern > suffix:
      left = mid + 1
    else:
      right = mid - 1
  return False

# Example usage
if __name__ == "__main__":
  text = "ACGTACGTACGT$"
  suffix_array = build_suffix_array(text)
  patterns = ["TAC", "CGT", "AAA"]
  for pattern in patterns:
    exists = pattern_exists(text, pattern, suffix_array)
    print(f"Pattern '{pattern}' exists: {exists}")
