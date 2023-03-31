names = input("Enter a list of names, separated by commas: ")


name_list = [name.strip() for name in names.split(",")]


name_list.sort()


print("Sorted list of names:")
for name in name_list:
    print(name)
