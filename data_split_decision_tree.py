#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris


# In[3]:


iris=load_iris()


# In[4]:


features=iris.data


# In[5]:


labels= iris.target


# In[6]:


#To divide data into traning and testing
from sklearn.model_selection import train_test_split


# In[13]:


X,Y,x,y=train_test_split(features,labels,test_size=0.2)
#0.0 - nothing is for testing ,0.1 - 10% data for testing ,1.0 -all data is for testing
#Also use train_size
#divides data in 4 parts
'''
X is 80% traning data with features
x is 20% training data with labels
Y is 80% testing data with features
y is 20% testing data with labels
features_train,features_test,labels_train,labels_test=train_test_split
'''
#random-state=100


# In[14]:


from sklearn.tree import DecisionTreeClassifier


# In[15]:


declf=DecisionTreeClassifier()


# In[16]:


trained = declf.fit(X,x)


# In[17]:


output = trained.predict(Y)


# In[18]:


output


# In[19]:


y


# In[20]:


from sklearn.metrics import accuracy_score
print(accuracy_score(y,output))


# In[ ]:




