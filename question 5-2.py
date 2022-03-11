#!/usr/bin/env python
# coding: utf-8

# In[3]:


def shape_data(shape: str, p1: int, p2: int = None):
    if shape == 'circle' and not p2:
        print(('C: %s' % (2 * 3.1416 * p1), 'A: %s' % (3.1416 * p1 * p1)))
    elif shape == 'rectangle' and p2:
        print(('P: %s' % (2 * (p1 + p2)), 'A: %s' % (p1 * p2)))



    


# In[5]:


shape_data('circle', 15)


# In[10]:


shape_data('rectangle', 20, 10)


# In[ ]:




