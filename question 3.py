#!/usr/bin/env python
# coding: utf-8

# In[1]:


def case_count(s):
    lower_num = 0
    upper_num = 0
    for letter in s:
        if 97 <= ord(letter) <= 122:
            lower_num += 1
        elif 65 <= ord(letter) <= 90:
            upper_num += 1
    print(('Uppercase: %s' % upper_num, 'Lowercase: %s' % lower_num))


# In[2]:


case_count('hello world')


# In[3]:


case_count('Hello World')


# In[ ]:




