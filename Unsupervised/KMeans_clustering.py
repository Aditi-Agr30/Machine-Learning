#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Kmeans clustering

#Handling data
import pandas as pd


# In[19]:


#Loading dataset
df = pd.read_csv('C:/Users/Aditi Agrawal/Desktop/ML_data/Unsupervised/mallanalysis.csv')


# In[20]:


#Printing metadata
df.info()


# In[21]:


#Printing top 5 data
df.head()


# In[22]:


#By manual analysis we have to decide right columns
useful_data=df.iloc[:,[3,4]].values


# In[23]:


#Now finding no. of cluster and analyzing it by elbow method
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[24]:


#Analysing Kmeans
#KMeans()

wcss=[]
for i in range(1,11):
    mykm=KMeans(n_clusters=i)
    #Now applying this state to data
    mykm.fit(useful_data)
    #inertia means summary of formula
    wcss.append(mykm.inertia_)
print(wcss)


# In[25]:


#Plotting graph - no. of clusters vs wcss
plt.xlabel("No. of cluster")
plt.ylabel("WCSS")
plt.plot(range(1,11),wcss,label="wcss with cluster no. using K-means++")
plt.legend()
plt.show()


# In[26]:


#Now we can assume no. of cluster as 5
#Again calling Kmeans
perfect_cls=KMeans(n_clusters=5)


# In[27]:


#Now applying data for clustering
predicted=perfect_cls.fit_predict(useful_data)


# In[28]:


#Now visualizing output
plt.xlabel('Income')
plt.ylabel('Spending score')
plt.title('Kmeans prediction')
#For cluster 0
plt.scatter(useful_data[ predicted == 0 ,0 ],useful_data[ predicted == 0 ,1],label='Smart customer')
plt.scatter(useful_data[ predicted == 1 ,0],useful_data[ predicted == 1 ,1],label='Target customer')
plt.scatter(useful_data[ predicted == 2 ,0],useful_data[ predicted == 2 ,1],label='Average customer')
plt.scatter(useful_data[ predicted == 3 ,0],useful_data[ predicted == 3 ,1],label='Ok Ok customer')
plt.scatter(useful_data[ predicted == 4 ,0],useful_data[ predicted == 4 ,1],label='Careless customer')
plt.legend()
plt.show()


# In[ ]:




