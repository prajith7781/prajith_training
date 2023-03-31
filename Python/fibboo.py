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