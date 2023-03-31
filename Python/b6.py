# Ask the user for input and convert it to a list of words
input_str = input("Enter a list of words separated by spaces: ")
words = input_str.split()

# Find the longest word in the list
longest_word = max(words, key=len)

# Print the longest word
print("The longest word in the list is:", longest_word)
