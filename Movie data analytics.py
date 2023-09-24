#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd 
import numpy as np
import seaborn as sns

import matplotlib
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from matplotlib.pyplot import figure 
pd.set_option('display.max_columns', None)






# In[76]:


data = pd.read_csv('movies.csv')


# In[42]:


data.shape


# #### Find out the number of missing data in each columns 

# In[14]:


data.isnull().sum()


# In[16]:


# Check the data type of the data set

data.dtypes


# In[25]:


# Changing the data type of the data column

data['budget'] = data['budget'].fillna(0)  
data['budget'] = data['budget'].astype('int64')
data['gross'] = data['gross'].fillna(0)  
data['gross'] = data['gross'].astype('int64')


# In[28]:


data


# #### Sort the top 5 movies whith highest revenue 

# In[46]:


revenue_movie = data.sort_values( by = 'gross', ascending = False )


# In[47]:


revenue_movie


# #### Drop any duplicated values 

# In[41]:


# Check to see if two rows are excatly the same 

data.drop_duplicates()


# In[43]:


data.shape 


# #### Find out the correlation betwenn data column

# ##### Q.1 Find out if there is correlation between budget and revenue of a moive 

# In[65]:


data.plot(kind = 'scatter', x = 'budget', y = 'gross', title = 'Budget vs Gross earning ')

plt.xlabel('Gross earning')
plt.ylabel('Budget for file')

plt.plot()


# In[66]:


# Show the top 20 movie that are having the highest revenue 

revenue_movie.head(20).plot(kind = 'scatter', x = 'budget', y = 'gross', title = 'Budget vs Gross earning ')

plt.xlabel('Gross earning')
plt.ylabel('Budget for file')

plt.plot()


# In[62]:


# Use a regression plot to show the correlation

sns.regplot(x = 'budget', y = 'gross', data = data, line_kws = { 'color' : 'blue'})


# In[67]:


data.corr(method = 'pearson')


# In[71]:


# Showing gross profit and budget are having a relative correlation by using a heatmap

corr_martrix = data.corr(method = 'pearson')

sns.heatmap(corr_martrix , annot = True)
plt.title('Correlation Matric for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.plot()


# In[72]:


data 


# In[82]:


# Change the data type of the whole data into numeric and show the data corr of the whole data set

data_numeric = data

for col_name in data_ncumeric.columns :
    if (data_numeric[col_name].dtype =='object'):
        data_numeric[col_name] = data_numeric[col_name].astype('category')
        data_numeric[col_name] = data_numeric[col_name].cat.codes
        
data_numeric


        


# In[83]:


data_numeric = data.corr(method = 'pearson')

sns.heatmap(data_numeric , annot = True)
plt.title('Correlation Matric for Numeric Features')
plt.xlabel('Movie Features')
plt.ylabel('Movie Features')

plt.plot()


# In[85]:


corr_matrics = data_numeric.corr()

corr_pairs = corr_matrics.unstack()

corr_pairs


# In[90]:


sort_corr = corr_pairs.sort_values()
high_corr = sort_corr[(sort_corr) > 0.5]
high_corr


# In[ ]:




