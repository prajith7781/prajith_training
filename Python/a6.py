num_list = input("Enter a list of numbers, separated by commas: ").split(",")
num_list = [float(num.strip()) for num in num_list]

largest = max(num_list)
smallest = min(num_list)


print("The largest number in the list is", largest, ".")
print("The smallest number in the list is", smallest, ".")
