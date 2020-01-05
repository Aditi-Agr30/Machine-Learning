#!/usr/bin/env python
# coding: utf-8

# In[8]:


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score #accuracy calculator


# In[9]:


iris=load_iris()   #datapct=sys.argv[1]


# In[10]:


dir(iris)


# In[11]:


features=iris.data
#Here all attributes of iris flower


# In[12]:


#if want to check data
iris.feature_names


# In[13]:


#class or label
labels=iris.target


# In[14]:


# Data visualization
plt.xlabel("Sepal & Petal length")
plt.ylabel("Sepal & Petal width")
plt.scatter(features[:,0],features[:,1],label="Sepal length & Sepal width",marker="*")
plt.scatter(features[:,2],features[:,-1],label="Petal length and width")
plt.legend()
plt.show()


# In[15]:


#Data splitting
dtrain,dtest,ltrain,ltest = train_test_split(features,labels)
# First two will be data
# Last two will be labels
#dtrain,dtest,ltrain,ltest = train_test_split(features,labels,test_size=datapct)


# In[16]:


dtrain.shape


# In[18]:


ltrain.shape


# In[19]:


#Now calling dtc with gini index
g_clf = DecisionTreeClassifier(criterion ="gini")


# In[20]:


#Calling dtc with entropy
e_clf = DecisionTreeClassifier(criterion="entropy")


# In[21]:


#Now training data
g_trained = g_clf.fit(dtrain,ltrain)


# In[22]:


e_trained = e_clf.fit(dtrain,ltrain)


# In[23]:


# Now predicting with gini index
g_out = g_trained.predict(dtest)


# In[24]:


# Predicting using entropy
e_out = e_trained.predict(dtest)


# In[25]:


# Calculating accuracy by gini
g_accuracy = accuracy_score(ltest,g_out)


# In[28]:


# Calculating accuracy by entropy
e_accuracy = accuracy_score(ltest,e_out)


# In[29]:


plt.pie([g_accuracy,e_accuracy],labels=["Gini","Entropy"],shadow=True,autopct="%1.1f%%",explode=(0,0.2))
plt.show()


# In[ ]:




