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


#     As it can be seen data frame that is above, we have 4 features that are movie id, title user id and rating
#     According to these data frame, we will make item based recommendation system
#     Lets look at shape of the data. The number of sample in data frame is 20 million that is too much. There can be problem in kaggle even if their own desktop ide's like spyder or pycharm.
#     Therefore, in order to learn item based recommendation system lets use 1 million of sample in data.



data = data.iloc[:1000000,:]


# In[13]:

# lets make a pivot table in order to make rows are users and columns are movies. And values are rating
pivot_table = data.pivot_table(index = ["userId"],columns = ["title"],values = "rating")
pivot_table.head(10)


# In[17]:


#     As it can be seen , rows are users, columns are movies and values are ratings
#     For example user 11 gives 3.5 rating to movie "Ace Ventura: When Nature Calls (1995)" and gives 3.0 rating to movie "Bad Boys (1995)".
#     Now lets make a scenario, we have movie web site and "Bad Boys (1995)" movie are watched and rated by people. The question is that which movie do we recommend these people who watched "Bad Boys (1995)" movie.
#     In order to answer this question we will find similarities between "Bad Boys (1995)" movie and other movies.



movie_watched = pivot_table["Bad Boys (1995)"]
similarity_with_other_movies = pivot_table.corrwith(movie_watched)  # find correlation between "Bad Boys (1995)" and other movies
similarity_with_other_movies = similarity_with_other_movies.sort_values(ascending=False)
similarity_with_other_movies.head()


# In[ ]:




