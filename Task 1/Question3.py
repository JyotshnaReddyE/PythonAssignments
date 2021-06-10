#Swap two numbers using a third variable and do the same task without using any third variable.

x= 10
y= 20
#using third variable
temp=x
x=y
y=temp
print("The value of x after swap =", x)
print("The value of y after swap =", y)
#without using third variable
x=30
y=40
x=x+y
y=x-y
x=x-y
print("The value of x after swap =", x)
print("The value of y after swap =", y)