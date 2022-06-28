#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1.Write a Python Program to Find the Factorial of a Number?
i=int(input("Enter the number of your choice:"))
if i<0:
    print("Factorial of your number does not exist")
    if i==0:
        print("factorial of the given number is 1")
else:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print("Factorial of given number is:",fact)


# In[11]:


#2.Write a Python Program to Display the multiplication Table?
i=int(input("Enter the number of your choice:"))
for j in range(1,11):
    print(j*i)


# In[5]:


#3.Write a Python Program to Print the Fibonacci sequence?
i=int(input("Enter the number of your choice:"))
k=0
j=1
count=0
while count<i:
    print(k)
    l=j+k
    k=j
    j=l
    count=count+1  


# In[9]:


#4.Write a Python Program to Check Armstrong Number?
num=int(input("Enter the number for check:"))
n=len(str(num))
temp=num
add=0
while temp!=0:
    l=temp%10
    add +=l**n
    temp=temp//10
if add==num:
    print("Given number is",num,"armstrong number")
else:
    print("Given number is",num,"not armstrong number")


# In[3]:


#5.Write a Python Program to Find Armstrong Number in an Interval?
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for num in range(lower,upper+1):
    n=len(str(num))
    temp=num
    add=0
    while temp!=0:
        l=temp%10
        add +=l**n
        temp=temp//10
    if add==num:
        print(num)


# In[16]:


#6.Write a Python Program to Find the Sum of Natural Numbers?
i=int(input("Enter the natural number for the addition task:"))
if i<0:
    print("Enter the positive number")
else:
    add=0
    while i>0:
        add= add+i
        i=i-1
    print("The addition of given natural numbers is:",add)

