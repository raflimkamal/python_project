#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install instaloader


# In[4]:


import instaloader


# In[6]:


ig = instaloader.Instaloader()
dp = input("Enter Insta Username:")

ig.download_profile(dp, profile_pic_only = True)


# In[ ]:




