#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

#Creating data
x=np.arange(0,100,5)
x1=np.arange(0,100,4)
y=[i for i in range(len(x))]
y1=[i for i in range(len(x1))]

plt.xlabel("Random x")
plt.ylabel("Random y")
plt.xlim(0,100)      #Here setting limit of x & y axis nos.
plt.ylim(0,30)

plt.plot(x,y,label="Numpy Data View")
plt.bar(x,y,label="Numpy Data View in bar")
plt.plot(x1,y1,label="Numpy Data View")
plt.legend()
plt.grid(color="green")
plt.show()


# In[2]:


len(x)


# In[3]:


[i for i in range(len(x))]


# In[15]:


import matplotlib.pyplot as plt

#Creating data
players = ["M.S.D","Virat"]
runs = [1200,1000]
runs1 = [1600,1300]
plt.xlabel("Players")
plt.ylabel("Score")

#Here setting limit of x & y axis nos.
plt.ylim(800,1400)
plt.bar(players,runs,label="Performance",color="blue")
plt.bar(players,runs1,label="Performance",color="red")
plt.grid(color="g")
plt.legend()
plt.show()


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
#Creating data
players = ["M.S.D","Virat","Rohit"]
runs = [1200,1000,1700]
runs1 = [1600,1300,1100]

#Subplot gives 2 properties
#fig is for entire figure
#ax is for individual attributes
fig,ax=plt.subplots(2)

#for graph 1 2019
ax[0].bar(players,runs,label="2019")
ax[0].set_title("Performance of 2019")
ax[0].legend()
#for graph 2 2020

ax[1].bar(players,runs1,label="2020")
ax[1].set_title("Performance of 2020")
ax[1].legend()
plt.show()


# In[34]:


import matplotlib.pyplot as plt
import numpy as np
#Creating data
players = ["M.S.D","Virat","Rohit"]
runs = [1200,1000,1700]
runs1 = [1800,1600,1800]

fig,ax=plt.subplots(2)
ax[0].pie(runs,labels=players,shadow=True,autopct="%1.1f%%",explode=(0,0,0.1))

ax[1].pie(runs1,labels=players,shadow=True,autopct="%1.1f%%",explode=(0.1,0,0))

"""plt.xlabel("Players")
plt.ylabel("Score")
plt.pie(runs,labels=players,shadow=True,autopct="%1.1f%%",explode=(0,0,0.1))
plt.pie(runs,labels=players,shadow=True,autopct="%1.1f%%",explode=(0,0,0.1))"""

plt.legend()
plt.show()


# In[38]:


import numpy as np
import matplotlib.pyplot as plt

#Creating data
x=np.arange(0,100,5)
x1=np.arange(0,100,4)
y=[i for i in range(len(x))]
y1=[i for i in range(len(x1))]

plt.xlabel("Random x")
plt.ylabel("Random y")
plt.xlim(0,100)      #Here setting limit of x & y axis nos.
plt.ylim(0,30)

plt.scatter(x,y,label="Normal way",marker="*")
plt.scatter(x1,y1,label="Danger")
plt.legend()
plt.grid(color="green")
plt.show()


# In[ ]:




