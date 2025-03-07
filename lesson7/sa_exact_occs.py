def build_suffix_array(text):
  suffixes = sorted((text[i:], i) for i in range(len(text)))
  return [idx for suffix, idx in suffixes]


def find_all_occurrences(text, pattern, sa):
  occurrences = []
  left, right = 0, len(sa) - 1
  while left <= right:
    mid = (left + right) // 2
    suffix = text[sa[mid]:]
    if suffix.startswith(pattern):
      # Explore neighbors for all matches
      occurrences.append(sa[mid])
      # Check left neighbors
      l_it = mid - 1
      while l_it >= left and text[sa[l_it]:].startswith(pattern):
        occurrences.append(sa[l_it])
        l_it -= 1
      # Check right neighbors
      r_it = mid + 1
      while r_it <= right and text[sa[r_it]:].startswith(pattern):
        occurrences.append(sa[r_it])
        r_it += 1
      break
    elif pattern > suffix:
      left = mid + 1
    else:
      right = mid - 1

  return sorted(occurrences)


# Example usage
if __name__ == "__main__":
  text = "ACGTACGTACGT$"
  suffix_array = build_suffix_array(text)
  patterns = ["TAC", "CGT", "AAA"]
  for pattern in patterns:
    positions = find_all_occurrences(text, pattern, suffix_array)
    if positions:
      print(f"Pattern '{pattern}' found at positions: {positions}")
    else:
      print(f"Pattern '{pattern}' not found.")
