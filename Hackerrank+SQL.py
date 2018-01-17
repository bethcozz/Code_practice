
# coding: utf-8

# In[1]:


'''
Query all columns for all American cities in CITY with populations larger than 100000. 
The CountryCode for America is USA.

Input Format

The CITY table is described as follows: 
Field / Type
ID / number
name / varchar
countrycode / varchar
district / varchar
population / number
'''


# In[ ]:


SELECT * FROM CITY
WHERE COUNTRYCODE = 'USA' AND POPULATION > 100000;


# In[ ]:


'''
Query the names of all American cities in CITY with populations larger 
than 120000. The CountryCode for America is USA.
'''


# In[ ]:


SELECT name FROM city
WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;

