
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import locale
import pixiedust


# In[46]:


from locale import atof


# In[47]:


locale.setlocale(locale.LC_NUMERIC, '')


# In[48]:


df_2006 = pd.read_csv('GDP_2006_16.csv')

df_2006 = df_2006.drop([0, 1, 2])
df_2006 = df_2006.set_index('Table of contents')
df_2006 = df_2006.rename(columns={"Unnamed: 1": "2006", "Unnamed: 2": "2007", "Unnamed: 3": "2008", "Unnamed: 4": "2009", "Unnamed: 5": "2010", "Unnamed: 6": "2011", "Unnamed: 7": "2012", "Unnamed: 8": "2013", "Unnamed: 9": "2014", "Unnamed: 10": "2015", "Unnamed: 11": "2016"})
df_2006 = df_2006.dropna(axis=0)
df_2006.index.name = "Table"
df_2006_t = df_2006.transpose()
help(df_2006_t)


# In[49]:


df_2006_t


# In[50]:


col_list1 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'hi','hi','hi','hi','power','hi','hi', 'hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','government', 'hi', 'hi', 'hi', 'sevices','hi','hi', 'gdp_market_price','hi'])
df_2006_t.columns = col_list1


# In[51]:


df_2006_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_2006_t  


# In[52]:


df_99 = pd.read_csv('GDP_99_10 .csv', thousands=',')
df_99 = df_99.dropna(axis=0)
df_99 = df_99.rename(columns={"Table 3 - Gross Domestic Product by industry group at current basic prices, 1999 - 2010": "Table"})
df_99 = df_99.set_index('Table')
df_99 = df_99.rename(columns={"Unnamed: 1": "1999", "Unnamed: 2": "2000", "Unnamed: 3": "2001", "Unnamed: 4": "2002", "Unnamed: 5": "2003", "Unnamed: 6": "2004", "Unnamed: 7": "2005", "Unnamed: 8": "2006", "Unnamed: 9": "2007", "Unnamed: 10": "2008", "Unnamed: 11": "2009", "Unnamed: 12": "2010"})
df_99_t = df_99.transpose()
df_99_t


# In[53]:


col_list2 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'hi','hi','hi','hi','power','hi','hi', 'hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','government', 'hi', 'hi',  'sevices','hi','hi', 'gdp_market_price','hi'])
df_99_t.columns = col_list2


# In[54]:


df_99_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_99_t
df_99_t.shape


# In[55]:


df_76 = pd.read_csv('GDP_76_98.csv', thousands=',')
df_76 = df_76.dropna(axis=0)
df_76 = df_76.rename(columns={"GROSS DOMESTIC PRODUCT BY INDUSTRY GROUP AT CURRENT PRICES (RS MN),1976 - 1998": "Table"})
df_76 = df_76.set_index('Table')
df_76 = df_76.rename(columns={"Unnamed: 1": "1976", "Unnamed: 2": "1977", "Unnamed: 3": "1978", "Unnamed: 4": "1979", "Unnamed: 5": "1980", "Unnamed: 6": "1981", "Unnamed: 7": "1982", "Unnamed: 8": "1983", "Unnamed: 9": "1984", "Unnamed: 10": "1985", "Unnamed: 11": "1986", "Unnamed: 12": "1987", "Unnamed: 13": "1988", "Unnamed: 14": "1989", "Unnamed: 15": "1990", "Unnamed: 16": "1991", "Unnamed: 17": "1992", "Unnamed: 18": "1993", "Unnamed: 19": "1994", "Unnamed: 20": "1995", "Unnamed: 21": "1996", "Unnamed: 22": "1997", "Unnamed: 23": "1998"})
df_76_t = df_76.drop(labels = ['INDUSTRY GROUP'])
df_76_t = df_76_t.transpose()
df_76_t


# In[56]:


df_76_t.columns
col_list3 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'power','hi','hi', 'hi','government', 'hi', 'hi', 'hi', 'hi','hi','hi','hi','hi','hi', 'sevices', 'gdp_market_price','hi', 'hi' ])
df_76_t.columns = col_list3


# In[57]:


df_76_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_76_t  


# In[58]:



df_48 = pd.read_csv('GDP_48_75.csv', thousands=',')
df_48 = df_48.dropna(axis=0)
df_48 = df_48.rename(columns={"Table 1 - Gross Domestic Product by Industrial Origin at current factor cost, 1948 - 1975": "Table"})
df_48 = df_48.set_index('Table')
df_48 = df_48.rename(columns={"Unnamed: 1": "1948", "Unnamed: 2": "1949", "Unnamed: 3": "1950", "Unnamed: 4": "1951", "Unnamed: 5": "1952", "Unnamed: 6": "1953", "Unnamed: 7": "1954", "Unnamed: 8": "1955", "Unnamed: 9": "1956", "Unnamed: 10": "1957", "Unnamed: 11": "1958", "Unnamed: 12": "1959", "Unnamed: 13": "1960", "Unnamed: 14": "1961", "Unnamed: 15": "1962", "Unnamed: 16": "1963", "Unnamed: 17": "1964", "Unnamed: 18": "1965", "Unnamed: 19": "1966", "Unnamed: 20": "1967", "Unnamed: 21": "1968", "Unnamed: 22": "1969", "Unnamed: 23": "1970", "Unnamed: 24": "1971", "Unnamed: 25": "1972", "Unnamed: 26": "1973", "Unnamed: 27": "1974", "Unnamed: 28": "1975"})
df_48_t = df_48.transpose()
df_48_t


# In[59]:


col_list4 = pd.Series(['agriculture', 'hi', 'mining', 'manufacturing', 'hi', 'power','hi', 'government', 'hi', 'hi', 'hi', 'hi', 'sevices', 'gdp_market_price','hi', 'hi' ])
df_48_t.columns = col_list4


# In[60]:


df_48_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_48_t  


# In[61]:


df_GDP = pd.concat([df_48_t, df_76_t, df_99_t, df_2006_t], axis = 0)



# In[62]:


type(df_GDP.agriculture[73])


# In[63]:




df_GDP = df_GDP.drop(['1948', '1949'], axis = 0)
#df_GDP = df_GDP.replace(',', '')
#df_GDP = df_GDP.float()
df_GDP


# In[ ]:


df_GDP.agriculture[i].astype(float);


# In[64]:


get_ipython().run_cell_magic('pixie_debugger', ' ', "def my_containsAny(str, set):\n    for c in set:\n        if c in str: return 1;\n    return 0;\n\nfor i in df_GDP.agriculture:\n    if isinstance(df_GDP.agriculture[i], str) == True:\n        if my_containsAny(i, ',') == 1:\n            df_GDP.agriculture[i].str.replace(',', ' ');\n            df_GDP.agriculture[i].astype(float);\n        else:\n            df_GDP.agriculture[i].astype(float);\n    else:\n        print('hi');\n    \n           \n            \n            \n        \n\n#df_GDP['agriculture'] = df_GDP['agriculture'].str.replace(',', ' ')\ndf_GDP\n#\n#df_GDP.plot()")


# In[65]:


df_GDP.plot()


# In[ ]:


df_GDP['agriculture'] = df_GDP['agriculture'].astype(int)


# In[ ]:


df_GDP.

