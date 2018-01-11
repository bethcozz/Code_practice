
# coding: utf-8

# In[2]:


indeed.isnull().any()


# In[ ]:


indeed['revenue2']=indeed['revenue'].fillna(0)
indeed.describe()


# In[ ]:


indeed['anyfirstrev']=indeed['first_revenue_date'].fillna(0)
indeed['anyfirstrev'].head(20)


# In[ ]:


indeed['anyfirstrev'] = np.where(indeed['anyfirstrev']!=0, 1, 0)
indeed.head(10)


# In[ ]:


indeed.duplicated('advertiser_id')
ad_dups = indeed.advertiser_id[indeed.advertiser_id.duplicated()].values
ad_dups


# In[ ]:


indeed.groupby('assigned').describe()
indeed.groupby('assigned').mean()


# In[ ]:


table = pd.crosstab(indeed.assigned, indeed.revenue)
chi2, p, dof, expected = chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p))


# In[ ]:


get_ipython().magic('matplotlib inline')
indeed.plot(kind='scatter', x='age', y='revenue', c=['darkgray'], s=20)
plt.xlabel('Age of Account')
plt.ylabel('Revenue') 
plt.title('Relationship Between Account Age and Revenue')
plt.show()


# In[ ]:


pearsonr_coefficient, p_value = pearsonr(indeed.age, indeed.revenue2)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))


# In[ ]:


indeed_trim = indeed[['assigned', 'age', 'assign_days', 'revenue2', 'anyfirstrev']]
indeed_trim.head(10)


# In[ ]:


X = indeed_trim
corr = X.corr()
corr
sb.heatmap(corr,xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()


# In[ ]:


y = indeed_trim.revenue2
X = indeed_trim.drop(['revenue2'], axis=1)


# In[ ]:


results = sm.OLS(y, X).fit()
results.summary()


# In[ ]:


indeed['anyrev'] = np.where(indeed['revenue2']!=0, 1, 0)


# In[ ]:


indeed_trim = indeed[['assigned', 'age', 'assign_days', 'anyrev', 'anyfirstrev']]

y = indeed_trim.anyrev
X = indeed_trim.drop(['anyrev'], axis=1)


# In[ ]:


logit = sm.Logit(y, X)
result = logit.fit()
print(result.summary())


# In[ ]:


print(np.exp(result.params))

