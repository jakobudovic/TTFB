from collections import Counter

def q_gram_match(T, P, q, m):
    """Uses the q-gram lemma to assess if P occurs in T with at most k edits."""
    n = len(P)
    num_qgrams_needed = max(1, n - q + 1 - m * q)  # Minimum q-gram matches required
    # Generate q-grams for P
    P_qgrams = [P[i:i+q] for i in range(len(P) - q + 1)]
    P_qgram_counts = Counter(P_qgrams)
    # Generate q-grams for T
    T_qgrams = [T[i:i+q] for i in range(len(T) - q + 1)]
    T_qgram_counts = Counter(T_qgrams)
    # Count how many q-grams in P appear in T
    matching_qgrams = sum(min(P_qgram_counts[qgram], T_qgram_counts.get(qgram, 0)) for qgram in P_qgram_counts)
    # Decision based on q-gram lemma
    return matching_qgrams >= num_qgrams_needed

# Example Usage:
T = "GATCACAGGTCTATCACCCTATTAACCACT"
#           ||| |||||| ||
P =        "GGTGTATCACTCT"
q = 3
m = 1

result = q_gram_match(T, P, q, m)
print(f"Does P appear in T with ≤ {m} edits? {result}")
