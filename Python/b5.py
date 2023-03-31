input_str1 = input("Enter the first list of numbers separated by spaces: ")
input_str2 = input("Enter the second list of numbers separated by spaces: ")
list1 = [int(num) for num in input_str1.split()]
list2 = [int(num) for num in input_str2.split()]


common_elements = [num for num in list1 if num in list2]

print("The common elements between the two lists are:", common_elements)
