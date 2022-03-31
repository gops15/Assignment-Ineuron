#!/usr/bin/env python
# coding: utf-8

# In[1]:


""" Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line."""


# In[8]:


nl = []
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        nl.append(str(i)) #append -  adds a single item to the existing list
print (','.join(nl))
    


# In[10]:


"""Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name."""


# In[17]:


x=input("Enter your First Name: ") #accepting the user's first and last name
y=input("Enter your Last Name:")

User_name=x+' '+y
print("Output:")
print("User Full Name :",User_name)
print("User Name in reverse order is :",User_name[::-1]) # reversing [::-1]


# In[ ]:


"""Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3*π*r^3"""


# In[23]:


import math
r = 12/2 ;
V=4/3*math.pi*r**3;
print(V)


# In[ ]:




