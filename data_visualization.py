#!/usr/bin/env python
# coding: utf-8

# In[1]:


#visualization
import matplotlib.pyplot as plt


# In[2]:


x=[2,8]   #x1 & x2
x1=[1,5]
y=[12,30]  #y1 & y2
y1=[4,6]


# In[3]:


plt.xlabel("Time")
plt.ylabel("Dist")
plt.plot(x,y,label="Speed of car")  #it will draw a line
plt.plot(x1,y1)
plt.grid(color="green")   #to draw grids
plt.legend()
plt.show()
#this is for line representation


# In[4]:


plt.xlabel("Time")
plt.ylabel("Dist")
plt.bar(x,y,label="Speed of car")  #it will draw a line
plt.bar(x1,y1)
plt.plot(x,y,label="Speed of car1")
plt.plot(x1,y1)
plt.grid(color="green")   #to draw grids
plt.legend()
plt.show()
#bar graph representation


# In[ ]:




