# Ask the user for input
input_str = input("Enter a string: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize an empty string to store the new string without vowels
new_str = ""

# Loop through each character in the input string
for char in input_str:
    # Check if the character is a vowel
    if char not in vowels:
        # If it is not a vowel, add it to the new string
        new_str += char

# Print the new string without vowels
print("The new string without vowels is:", new_str)
