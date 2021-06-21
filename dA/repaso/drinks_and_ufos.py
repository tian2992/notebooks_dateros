#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# # Hoja de trabajo de UFOs y Bebidas
# 
# Cargamos los datos de consumo de bebidas y tipo por pais.
# 

# In[3]:


drinks = pd.read_csv("http://bit.ly/drinksbycountry")


# In[4]:


drinks


# Pensemos con estos datos que podemos extraer:
# 
# * porcentaje de consumo total por cada bebida
# * comparemos top de consumo por cada bebida
# * cuales son las bebidas favoritas de cada continente
# * etc
# 

# In[1]:


drinks.hist()


# # Ahora los a 🛸 UFOs 👽
# 
# Importamos los avistamientos. Pensemos que podemos extraer con este recurso.
# 👾

# In[2]:


ufos = pd.read_csv("http://bit.ly/uforeports")


# In[ ]:





# In[5]:





# 
