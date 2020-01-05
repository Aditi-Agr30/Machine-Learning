#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
df=pd.read_csv('C:/Users/Aditi Agrawal/Desktop/ML_data/info.csv')


# In[11]:


df.info()
#To print schema of csv file 


# In[12]:


newdata=df.values  # .values removes headers of rows and columns


# In[13]:


from sklearn.preprocessing import Imputer


# In[14]:


imp=Imputer(missing_values=np.nan,strategy='mean',axis=0)


# In[17]:


newdata[:,1:3]=imp.fit_transform(newdata[:,1:3])


# In[18]:


newdata


# In[ ]:




