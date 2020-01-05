#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#this supports local path as well as url
df=pd.read_csv('C:/Users/Aditi Agrawal/Desktop/ML_data/info.csv')


# In[3]:


df.head(3) #only top 3 lines


# In[4]:


df.head() #default 5 lines


# In[6]:


df['Country']


# In[7]:


df


# In[8]:


#specific rows and columns
df.iloc[0:3,0:3]


# In[10]:


df.iloc[1:4,0:2]


# In[11]:


df.iloc[[3,5],[1,2]].values


# In[12]:


max(df.Age)


# In[15]:


min(df.Age)


# In[16]:


[i for i in dir(pd) if 'read' in i]

