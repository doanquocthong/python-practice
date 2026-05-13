#Problem: Find the most frequent character in a string  

# Concept:
# Loop
# Dictionary
# String processing

def find_most_frequent_char(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    return max(freq, key = freq.get)

print(find_most_frequent_char("Programming"))