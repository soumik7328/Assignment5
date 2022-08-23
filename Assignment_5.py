#Assignment - 5 Full Stack Web Development using Python MySirG Operators
#1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
a=int(input("Enter a number:-"))
print(a//10)
#2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
a=int(input("Enter a number:-"))
print(a%10)
#3. Write a python script to swap data of two variables
a=eval(input("Enter a="))
b=eval(input("Enter b="))
d=a
a=b
b=d
print("a=",a,"b=",b)

#4. Write a python script to find x power y, where values of x and y are given by user
x=eval(input("Enter x="))
y=eval(input("Enter y="))
print("x power y= ",x**y)

#5. Write a python script which takes a three digit number from the user and displays only its first digit.
x=eval(input("Enter a three digit number:-"))
x=x//100
print("its first digit is=",x)

#6. Write a python script which takes a three digit number from the user and displays only its middle digit.
x=eval(input("Enter a three digit number:-"))
x=x//10
x=x%10
print("its middle digit is=",x)
#7. Write a python script which takes a three digit number from the user and displays only its last digit.
x=eval(input("Enter a three digit number:-"))
x=x%10
print("its last digit is=",x)
#8. Write a python script to use IN operator to display the data present in the list
list=[5,6,7,4]
a=eval(input("Enter a number:-"))
if a in list:
    print("Data present in the list")
else:
    print("Data not in list")    
#9. Write a python script to use NOT IN operator to display the data not present in list
list=[5,6,7,4]
a=eval(input("Enter a number:-"))
if a not in list:
    print("Data not present in the list")
else:
    print("Data in the list")  
#10. Write a python script to use IS operator to display if both variables are the same object or not?
a=eval(input("Enter a number"))
b=eval(input("Enter a number"))
if a is b:
    print("Both variables are the same object:-")
else:
    print("Both variable are not same object:-")