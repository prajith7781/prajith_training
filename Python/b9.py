# Ask the user for input and convert it to a list of integers
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, input_str.split()))

# Square each element in the list
squared_numbers = [num**2 for num in numbers]

# Print the list of squared numbers
print("The squared numbers are:", squared_numbers)
