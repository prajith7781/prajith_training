# Ask the user for input and convert it to a list of strings
input_str = input("Enter a list of strings separated by spaces: ")
strings = input_str.split()

# Sort the list of strings in alphabetical order
strings_sorted = sorted(strings)

# Print the sorted list of strings
print("The sorted list of strings is:", strings_sorted)
