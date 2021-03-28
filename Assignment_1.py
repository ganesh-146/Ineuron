#!/usr/bin/env python
# coding: utf-8

# #### 1 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line
# 

# In[33]:


#1
s = range(2000,3201)
r = []
for i in s:
    if (i % 7 == 0) and (i % 5 != 0):
        r.append(i)
print(r)   


# #### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[35]:


#2
a = input("Enter first name:")
b = input("Enter last name:")
c = a[::-1]
d = b[::-1]
print(c , d)


# #### 3. Write a Python program to find the volume of a sphere with diameter 12 cm Formula: V=4/3 * π * r 3

# In[39]:


#3
pi = 3.14
d = 12
r = d/2
v = (4 / 3) * pi * (r * r * r)
print("Volume of  the sphere is =",v )

