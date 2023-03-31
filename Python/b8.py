# Ask the user for input
input_str = input("Enter a string: ")

# Count the number of times each letter appears in the string
letter_counts = {}
for letter in input_str:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Print the letter counts
print("Letter counts:", letter_counts)
