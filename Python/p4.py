


# x = 5
# if x > 3:
#     print("x is greater than 3")






# x = 5
# if x > 10:
#     print("x is greater than 10")
# elif x > 3:
#     print("x is greater than 3")
# else:
#     print("x is less than or equal to 3")






# x = 5
# y = 10
# if x > 3 and y < 15:
#     print("Both conditions are true")



# x = 5
# y = 10
# if x > 3:
#     if y < 15:
#         print("Both conditions are true")





# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)





# i = 0
# while i < 5:
#     print(i)
#     i += 1
#-------------------------------Fibbo--------------------------------------

n = int(input("Enter the number of terms: "))


a, b = 0, 1


if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(a)
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(a)
       c = a + b
       
       a = b
       b = c





