#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


movie = pd.read_csv("movie.csv")
movie.columns


# In[6]:


movie = movie.loc[:,["movieId","title"]]
movie.head(10)


# In[7]:


rating = pd.read_csv("rating.csv")
rating.columns


# In[8]:


rating = rating.loc[:,["userId","movieId","rating"]]
rating.head(10)


# In[9]:


data = pd.merge(movie,rating)


# In[10]:


data.head(10)


# In[11]:


data.shape


# In[12]:


data = data.iloc[:1000000,:]


# In[13]:


pivot_table = data.pivot_table(index = ["userId"],columns = ["title"],values = "rating")
pivot_table.head(10)


# In[17]:


movie_watched = pivot_table["Angela (1995)"]
similarity_with_other_movies = pivot_table.corrwith(movie_watched)  # find correlation between "Bad Boys (1995)" and other movies
similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
similarity_with_other_movies.head()


# In[ ]:




