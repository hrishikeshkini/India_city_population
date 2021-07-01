#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import folium as fo
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


map = fo.Map()


# In[3]:


vol = fo.FeatureGroup(name='India City Population')


# In[4]:


vol.add_child(fo.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))


# In[5]:


map.add_child(vol)


# In[6]:


popu = pd.read_csv('in.csv')


# In[7]:


popu.head()


# In[8]:


popu.describe()


# In[9]:


lat_po = list(popu['lat'])
lon_po = list(popu['lng'])
name_po = list(popu['city'])
pop_po = list(popu['population'])


# In[10]:


po = fo.FeatureGroup(name='India City Population')


# In[14]:


def marks(popu):
    if(popu>1.014227e+06):
        return 'red'
    elif(popu>3.064090e+05 and popu<=1.014227e+06):
        return 'blue'
    else:
        return 'green'


# In[15]:


for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name] , 
                          icon=fo.Icon(color=marks(pop))))


# In[16]:


map.add_child(po)

