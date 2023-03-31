numbers = input("Enter a list of numbers, separated by commas: ")
number_list = numbers.split(",")

sum = 0
for num in number_list:
    if int(num) % 2 == 0:
        sum += int(num)

print("The sum of all even numbers in the list is:", sum)
