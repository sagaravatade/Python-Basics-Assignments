#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Write a Python Program to Find LCM?
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
def cal_lcm(a,b):
    if a>b:
        g=a
    else:
        g=b
    while(True):
        if((g%a==0)and(g%b==0)):
            lcm=g
            break
        g=g+1
    return lcm
print("LCM of two numbers is:", cal_lcm(a,b))


# In[10]:


#2.Write a Python Program to Find HCF?
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
def cal_hcf(a,b):
    if a>b:
        g=a
    else:
        g=b
    for i in range(1,g+1):
        if((a%i==0)and(b%i==0)):
            hcf=i
    return hcf
print("HCF of two numbers is:", cal_hcf(a,b))


# In[14]:


#3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
num=int(input("Enter the decimal number:"))
print("The binary conversion of given number is:",bin(num))
print("The octal conversion of given number is:",oct(num))
print("The hexadecimal conversion of given number is:",hex(num))


# In[29]:


#4.Write a Python Program To Find ASCII value of a character?
i=input("Enter the character:")
print("The ASCII value of",i,"is:",ord(i))


# In[1]:


#5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
# Program make a simple calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")


# In[ ]:




