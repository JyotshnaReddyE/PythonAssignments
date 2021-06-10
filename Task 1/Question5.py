#5. Write a program to complete the task given below:Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum inanother variable called z. Add 30 to z and store the output in variable result and print result as thefinal output.

x = int(input("Enter first number between 1-10:"))
y = int(input("Enter second number between 1-10:"))
z = x+y
print("z=",z)
result=z+30
print("Final output:", result)