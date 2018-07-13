
# coding: utf-8

# In[262]:


import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import locale
import pixiedust
import math


# In[263]:


from locale import atof


# In[264]:


locale.setlocale(locale.LC_NUMERIC, '')


# # ***all data entries are in millions of rupees***

# In[266]:


df_2006 = pd.read_csv('GDP_2006_16.csv')

df_2006 = df_2006.drop([0, 1, 2])
df_2006 = df_2006.set_index('Table of contents')
df_2006 = df_2006.rename(columns={"Unnamed: 1": "2006", "Unnamed: 2": "2007", "Unnamed: 3": "2008", "Unnamed: 4": "2009", "Unnamed: 5": "2010", "Unnamed: 6": "2011", "Unnamed: 7": "2012", "Unnamed: 8": "2013", "Unnamed: 9": "2014", "Unnamed: 10": "2015", "Unnamed: 11": "2016"})
df_2006 = df_2006.dropna(axis=0)
df_2006.index.name = "Table"
df_2006_t = df_2006.transpose()

col_list1 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'hi','hi','hi','hi','power','hi','hi', 'hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','government', 'hi', 'hi', 'hi', 'sevices','hi','hi', 'gdp_market_price','hi'])
df_2006_t.columns = col_list1

df_2006_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_2006_t.head()


# In[289]:


df_99 = pd.read_csv('GDP_99_10 .csv', thousands=',')

pd.options.display.max_rows = None
display(df_99)




# In[ ]:


df_99 = df_99.dropna(axis=0)
df_99 = df_99.rename(columns={"Table 3 - Gross Domestic Product by industry group at current basic prices, 1999 - 2010": "Table"})
df_99 = df_99.set_index('Table')
df_99 = df_99.rename(columns={"Unnamed: 1": "1999", "Unnamed: 2": "2000", "Unnamed: 3": "2001", "Unnamed: 4": "2002", "Unnamed: 5": "2003", "Unnamed: 6": "2004", "Unnamed: 7": "2005", "Unnamed: 8": "2006", "Unnamed: 9": "2007", "Unnamed: 10": "2008", "Unnamed: 11": "2009", "Unnamed: 12": "2010"})
df_99_t = df_99.transpose()
df_99_t.head()


# In[268]:


col_list2 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'hi','hi','hi','hi','power','hi','hi', 'hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','hi','government', 'hi', 'hi',  'sevices','hi','hi', 'gdp_market_price','hi'])
df_99_t.columns = col_list2


# In[269]:


df_99_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_99_t
df_99_t.shape


# In[270]:


df_76 = pd.read_csv('GDP_76_98.csv', thousands=',')
df_76 = df_76.dropna(axis=0)
df_76 = df_76.rename(columns={"GROSS DOMESTIC PRODUCT BY INDUSTRY GROUP AT CURRENT PRICES (RS MN),1976 - 1998": "Table"})
df_76 = df_76.set_index('Table')
df_76 = df_76.rename(columns={"Unnamed: 1": "1976", "Unnamed: 2": "1977", "Unnamed: 3": "1978", "Unnamed: 4": "1979", "Unnamed: 5": "1980", "Unnamed: 6": "1981", "Unnamed: 7": "1982", "Unnamed: 8": "1983", "Unnamed: 9": "1984", "Unnamed: 10": "1985", "Unnamed: 11": "1986", "Unnamed: 12": "1987", "Unnamed: 13": "1988", "Unnamed: 14": "1989", "Unnamed: 15": "1990", "Unnamed: 16": "1991", "Unnamed: 17": "1992", "Unnamed: 18": "1993", "Unnamed: 19": "1994", "Unnamed: 20": "1995", "Unnamed: 21": "1996", "Unnamed: 22": "1997", "Unnamed: 23": "1998"})
df_76_t = df_76.drop(labels = ['INDUSTRY GROUP'])
df_76_t = df_76_t.transpose()


pd.options.display.max_columns = None
display(df_76_t.head())


# In[271]:


df_76_t.columns
col_list3 = pd.Series(['agriculture', 'hi', 'hi','mining', 'manufacturing', 'power','hi','hi', 'hi','government', 'hi', 'hi', 'hi', 'hi','hi','hi','hi','hi','hi', 'sevices', 'gdp_market_price','hi', 'hi' ])
df_76_t.columns = col_list3


# In[272]:


df_76_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_76_t.head()


# In[273]:



df_48 = pd.read_csv('GDP_48_75.csv', thousands=',')
df_48 = df_48.dropna(axis=0)
df_48 = df_48.rename(columns={"Table 1 - Gross Domestic Product by Industrial Origin at current factor cost, 1948 - 1975": "Table"})
df_48 = df_48.set_index('Table')
df_48 = df_48.rename(columns={"Unnamed: 1": "1948", "Unnamed: 2": "1949", "Unnamed: 3": "1950", "Unnamed: 4": "1951", "Unnamed: 5": "1952", "Unnamed: 6": "1953", "Unnamed: 7": "1954", "Unnamed: 8": "1955", "Unnamed: 9": "1956", "Unnamed: 10": "1957", "Unnamed: 11": "1958", "Unnamed: 12": "1959", "Unnamed: 13": "1960", "Unnamed: 14": "1961", "Unnamed: 15": "1962", "Unnamed: 16": "1963", "Unnamed: 17": "1964", "Unnamed: 18": "1965", "Unnamed: 19": "1966", "Unnamed: 20": "1967", "Unnamed: 21": "1968", "Unnamed: 22": "1969", "Unnamed: 23": "1970", "Unnamed: 24": "1971", "Unnamed: 25": "1972", "Unnamed: 26": "1973", "Unnamed: 27": "1974", "Unnamed: 28": "1975"})
df_48_t = df_48.transpose()
df_48_t.head()


# In[274]:


col_list4 = pd.Series(['agriculture', 'hi', 'mining', 'manufacturing', 'hi', 'power','hi', 'government', 'hi', 'hi', 'hi', 'hi', 'sevices', 'gdp_market_price','hi', 'hi' ])
df_48_t.columns = col_list4


# In[275]:


df_48_t.drop(columns = ['hi'], axis = 1, inplace = True)
df_48_t .head()


# In[276]:


df_GDP = pd.concat([df_48_t, df_76_t, df_99_t, df_2006_t], axis = 0)
df_GDP = df_GDP.drop(['1948', '1949'], axis = 0)
df_GDP = df_GDP[~df_GDP.index.duplicated(keep='first')]


# In[277]:


df_GDP.index.rename('Years', inplace = True)
df_GDP.head()


# In[278]:


#removing the commas from the database

def my_containsAny(str, set):
    for c in set:
        if c in str: return 1;
    return 0

for column in df_GDP:
    index = -1
    for i in df_GDP[column]:
        index = index +  1
        if type(i) == str:
            #print("this is a string: " + i)
            if my_containsAny(i, ',') == 1:
                #print("replacing the commas in this string: ", i)
                i = i.replace(',', '')
                #print("this no longer has commas: " + i)
                i = float(i)
                #print("this was a string but now it is a float: %f, " % (i) )
                df_GDP[column][index] = i
            else: 
                i = float(i)
                df_GDP[column][index] = i
                #print("this was a string  but now it is a float: %f" % (i) 
                
    #print(df_GDP[column])


# In[279]:


# now graphs can be made
df_GDP


# In[280]:


# saving as CSV
df_GDP.to_csv('GDP.csv')


# In[281]:


df_GDP.plot()


# In[282]:


df_GDP2 = df_GDP.drop(columns="gdp_market_price")


# ## Gross Domestic Product, at the market price, over time 
# Figures shown in millions of rupees

# In[283]:


x = df_GDP.index
y = df_GDP['gdp_market_price']



fig = plt.figure(figsize=(40,10))
ax = fig.add_subplot(121)

# figure out number of data points to show 
ax.xaxis.set_major_locator(plt.MaxNLocator(10))

ax.tick_params(axis='x', labelsize=8)


plt.plot(x,y)
plt.show


# ## Growth of industries over time

# In[284]:


x = df_GDP2.index
y = df_GDP2

fig = plt.figure(figsize=(30,10))
ax = fig.add_subplot(121)

# number of data points to show 
ax.xaxis.set_major_locator(plt.MaxNLocator(20))

ax.tick_params(axis='x', labelsize=8)
# where is the legend????
plt.plot(x,y)
plt.show


# In[285]:


df_GDP.drop(columns="gdp_market_price").plot(figsize=(25,10), kind = 'bar')


# ## Change in percentage of GDP made up by each industry over time

# In[286]:


x50 = df_GDP2.loc['1950']
x70 = df_GDP2.loc['1970']
x90 = df_GDP2.loc['1990']
x2010 = df_GDP2.loc['2010']
x2016 = df_GDP2.loc['2016']

fig, axes = plt.subplots(5,  figsize=(5,20))



axes[0].pie(x50)
axes[0].set_title("1950")
axes[1].pie(x70)
axes[1].set_title("1970")
axes[2].pie(x90)
axes[2].set_title("1990")
axes[3].pie(x2010)
axes[3].set_title("2010")
axes[4].pie(x2016)
axes[4].set_title("2016")

#plt.title("Change in distribution of industry with respect to GDP")
plt.figlegend(list(df_GDP2.columns))


plt.show

