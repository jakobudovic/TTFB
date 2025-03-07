def build_suffix_array(text):
    text += "$"
    suffixes = [(text[i:], i) for i in range(len(text))]
    suffixes.sort()
    suffix_array = [idx for (suffix, idx) in suffixes]
    return suffix_array

def display_suffix_array(text,suffix_array):
    print("Suffix Array:")
    for idx in suffix_array:
        print(f"{idx}: {text[idx:]}$")

# Example usage
if __name__ == "__main__":
    input_text = "ACGTACGT"
    suffix_array = build_suffix_array(input_text)
    display_suffix_array(input_text,suffix_array)
