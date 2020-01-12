#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#Loading iris data
from sklearn.datasets import load_iris
#Loading other libraries
import matplotlib.pyplot as plt #For data visualization
from sklearn.tree import DecisionTreeClassifier #Decision tree
from sklearn.model_selection import train_test_split #Importing data split technique
from sklearn.metrics import accuracy_score #accuracy calculator


# In[2]:


#Loading csv file
df = pd.read_csv('C:/Users/Aditi Agrawal/Desktop/ML_data/social.csv')


# In[3]:


features = df.iloc[:,[2,3]].values


# In[4]:


#Importing svm
from sklearn.svm import SVC
labels = df.iloc[:,-1].values


# In[5]:


svc_clf=SVC(kernel='linear')


# In[6]:


#Splitting data into training and testing
X,x,Y,y = train_test_split(features,labels,test_size=0.2)


# In[ ]:


svc_trained = svc_clf.fit(X,Y)


# In[ ]:


#Now predicting 
output = svc_trained.predict(x)


# In[ ]:


accuracy_score(y,output)


# In[ ]:


#Finding confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y,output)


# In[ ]:


#Applying rbf kernel
svc_clf1 = SVC(kernel='rbf')


# In[ ]:


rclf = svc_clf1.fit(X,Y)


# In[ ]:


out = rclf.predict(x)


# In[ ]:


accuracy_score(y,out)


# In[ ]:




