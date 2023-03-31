# Ask the user for input and convert it to a list of integers
input_str = input("Enter a list of numbers: ")
numbers = [int(num) for num in input_str.split()]

# Initialize a variable to keep track of the sum of even numbers
sum_of_evens = 0

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # If it is even, add it to the sum_of_evens variable
        sum_of_evens += number

# Print the sum of even numbers
print("The sum of all even numbers in the list is:", sum_of_evens)
