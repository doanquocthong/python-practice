#Problem: Find the most frequent character in a string  

# Concept:
# Loop
# Dictionary
# String processing
text = "Programming"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

max_char = max(freq, key=freq.get)

print(max_char)