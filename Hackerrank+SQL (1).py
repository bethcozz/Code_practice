
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


# In[ ]:


#Query a count of the number of cities in CITY having a Population larger than 100,000.


# In[ ]:


SELECT COUNT(name) 
FROM city
WHERE population > 100000;


# In[ ]:


'''
#select sum total of populations in CA cities

SELECT SUM(population)
FROM city
WHERE district='California';
'''


# In[ ]:


'''
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where 
the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:
City (as above)

Country
Field / Type
code / varchar
name / varchar
continent / varchar
region / varchar
surfacearea / varchar
indepyear / varchar
population / number
lifeexpectancy / varchar
gnp / number
gnpold / number
localname / varchar
governmentform / varchar
headofstate / varchar
capital / varchar
code2 / varchar
'''


# In[ ]:


'''
SELECT SUM(POPULATION) 
FROM CITY 
WHERE COUNTRYCODE IN (SELECT CODE FROM COUNTRY WHERE CONTINENT = 'Asia')
'''


# In[ ]:


'''
SELECT city.name FROM city
JOIN country
    ON city.countrycode = country.code
WHERE country.continent = 'Africa';

### ORDER - SELECT, JOIN, ON, WHERE
'''


# In[2]:


# query names of all continents and avg city pops rounded down to nearest int
# DO NOT include continents w/o 


# In[ ]:


'''
SELECT c.continent,FLOOR(AVG(ci.population)) FROM city ci
INNER JOIN country c
ON ci.countrycode = c.code
GROUP BY c.continent;
'''


# In[ ]:


'''
CODE ACADEMY JOINS:

SELECT COUNT(id) FROM newspaper;
SELECT COUNT(id) FROM online;

##inner join:

SELECT COUNT(n.id) FROM newspaper n
JOIN online o
	ON n.id = o.id;

##left join, where we want only users who don't subscribe online:
    
SELECT * FROM newspaper n
LEFT JOIN online o
	ON n.id = o.id
WHERE o.id IS NULL; 

#inner join with primary and foreign keys

SELECT * FROM classes c
INNER JOIN students s
	ON c.id = s.class_id;
    
'''


# In[ ]:


'''
#ANSWERS:

-- First query
SELECT COUNT(*)
FROM newspaper
WHERE start_month < 3
	AND end_month > 3;
  
-- Second query  
SELECT *
FROM newspaper
CROSS JOIN months;

-- Third query
SELECT *
FROM newspaper
CROSS JOIN months
WHERE start_month < month
	AND end_month > month;

-- Fourth query
SELECT months.month,
	COUNT(*)
FROM newspaper
CROSS JOIN months
WHERE start_month < month
	AND end_month > month
GROUP BY months.month;
'''


# In[ ]:


'''
#Select count of all columns w/ subscribers in March
SELECT COUNT(*)
FROM newspaper n
WHERE n.start_month < 3 
AND n.end_month > 3;

#Cross join newspapers and month
SELECT * FROM newspaper n
CROSS JOIN months m;

#Cross join n and m only for months in b/w start and end dates
SELECT * FROM newspaper n
CROSS JOIN months m
WHERE n.start_month < m.month 
AND m.month < n.end_month;

#aggregate subscribers by month
SELECT month,
	COUNT(*) AS subscribers
FROM newspaper n
CROSS JOIN months m
WHERE n.start_month < m.month
AND m.month < n.end_month
GROUP BY m.month;
'''


# In[ ]:


'''
UNION = stack one data set on top of the other
RULES FOR APPENDING:
    - must have same # columns
    - cols must have same data type in same order
E.G.:
SELECT * 
FROM newspaper n
UNION 
SELECT *
FROM online o;

'''


# In[ ]:


'''
#NESTING COMMANDS WITHIN EACH OTHER

WITH previous_query AS (
SELECT customer_id,
       COUNT(subscription_id) as subscriptions
FROM orders
GROUP BY customer_id)
SELECT customers.customer_name,
previous_query.subscriptions
FROM previous_query
JOIN customers
	ON customers.customer_id = previous_query.customer_id;
    
'''

