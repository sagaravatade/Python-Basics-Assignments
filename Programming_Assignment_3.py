#!/usr/bin/env python
# coding: utf-8

# In[9]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=int(input("Enter the number of your choice:"))
if a>0:
    print("Entered number is Positive")
elif a<0:
    print("Entered number is Negative")
else:
    print("Entered number is Zero")


# In[12]:


#2. Write a Python Program to Check if a Number is Odd or Even?
b=int(input("Enter the number of your choice:"))
if a%2==0:
    print("Entered number is Even")
else:
    print("Entered number is Odd")


# In[15]:


#3. Write a Python Program to Check Leap Year?
c=int(input("Enter the year of your choice:"))
if ((c%4==0 and c%100!=0) or (c%400==0 and c%100==0)):
    print("entered year is Leap year")
else:
    print("Entered year is not Leap year")


# In[26]:


#4. Write a Python Program to Check Prime Number?
d=int(input("Enter the year of your choice:"))
if d>0:
    for i in range(2,d):
        if (d%i==0):
            print("Entered number is not prime number")
            break
    else:
        print("Entered number is prime number")
else:
    print("Enteresd number is not prime number")


# In[33]:


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
#lower=1
#upper=10000
for num in range(1,10001):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
            print(num)


# In[35]:


for i in range(2,4):
    print(i)


# In[20]:





# In[ ]:




