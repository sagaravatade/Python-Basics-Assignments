#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Write a Python program to print "Hello Python" ?
print("Hello Python")


# In[7]:


#2.Write a Python program to do arithmetical operations addition and division.?
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
print("addition of a+b=",a+b)
print("Division of a/b=",a/b)


# In[11]:


#3.Write a Python program to find the area of a triangle?
b=int(input("enter base of the triangle b="))
h=int(input("enter height of the triangle h="))
print("Area of the triangle=", (b*h/2),"square unit")


# In[7]:


#4.Write a Python program to swap two variables?
a=input("enter the value of a=")
b=input("enter the value of b=")
c=a
a=b
b=c
print("Swapped value of a=",a)
print("Swapped value of b=",b)


# In[11]:


#5.Write a Python program to generate a random number?
import random
a=random.randint(0,10)
print(a)

