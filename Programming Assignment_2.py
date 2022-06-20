#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Write a Python program to convert kilometers to miles?
a=float(input("Enter value in Kilometers="))
k=0.621371
print(a,"Kilometers is equal to",a*k,"miles")


# In[7]:


#2.Write a Python program to convert Celsius to Fahrenheit?
dc=float(input("Enter value of temperature in degree celsius="))
f=(dc*9/5)+32
print(dc,"degree celsius is equal to",f,"fahrenheit")


# In[16]:


#3. Write a Python program to display calendar?
import calendar
yy=int(input("Enter The year for which you want to display the calender:")) 
print(calendar.calendar(yy))


# In[5]:


#4.Write a Python program to solve quadratic equation?
import cmath
a=1
b=5
c=6
d=(b*b)-(4*a*c)
s1=(-b+cmath.sqrt (d))/(2*a)
s2=(-b-cmath.sqrt(d))/(2*a)
print("The roots of above equation are",s1,"&",s2)


# In[7]:


#5.Write a Python program to swap two variables without temp variable?
x=input("Enter the value of x:")
y=input("Enter the value of y:")
x,y=y,x
print("swapped value of x:",x)
print("swapped value of y:",y)


# In[ ]:




