#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s
from datetime import timedelta


# # Importing csv dataset

# In[18]:


df = pd.read_csv('Documents/encoded-Job opportunities.csv')
df


# In[19]:


df.tail(5)


# ### total no. of Rows and columns

# In[20]:


print('In this Dataset, the no of rows is ',df.shape[0], 'and no. of columns is ',df.shape[1])


# ### Checking for any presence of NULL values in this dataset

# In[21]:


df.isnull().sum()


# ##### thus no null values in this dataset

# In[ ]:





# ### Data Understanding and exploration Process

# In[22]:


df.info()


# In[23]:


df.describe().transpose()


# # Data cleaning

# In[24]:


df['Required Skills'] = df['Required Skills'].str.split(', ')

# Expand the 'Required Skills' column into separate rows and apply it to the original DataFrame
df = df.explode('Required Skills')


# In[25]:


df.head(5)


# In[26]:


df.info()


# In[ ]:





# ### cleaning salary column which is range and string to numeric for effective analysis.
# #### for that we cansplit it into 2 columns one is minimum package, other one maximum package of that role.

# In[27]:


df[['Min Salary', 'Max Salary']] = df['Salary Range'].str.replace(r'[\£,]', '', regex=True).str.split('-', expand=True)
df['Min Salary']= pd.to_numeric(df['Min Salary'])
df['Max Salary']= pd.to_numeric(df['Max Salary'])


# In[28]:


df.drop('Salary Range', axis=1,inplace = True)


# In[29]:


df.head(5)


# ## changing the date format

# In[30]:


df['Date Posted'] = pd.to_datetime(df['Date Posted'])


# In[31]:


df.head(5)


# In[32]:


print('In this Dataset, the no of rows is ',df.shape[0], 'and no. of columns is ',df.shape[1])


# # Data Analysis

# ## how many Unique jobs are there in the IT sector feild

# In[33]:


jobs = df['Job Title'].unique().tolist()
print('the total no of unique jobs are ',len(jobs),'\n\n\n','They are:')
jobs


# ### top 10 In-Demand Job Roles

# In[34]:


jobs_chart = df['Job Title'].value_counts().head(10)
jobs_chart.plot(kind = 'bar', color = 'Red')
plt.xlabel('Top 10 Demanded Job Roles')
plt.ylabel('Number of Listing')
plt.title('Top 10 Demanded Job Roles and their Listing')
plt.show()


# ### Top 10 most demand skill

# In[35]:


newdf = pd.DataFrame(df['Required Skills'].value_counts().head(10))


# In[36]:


newdf.plot(kind='bar', color = 'Blue')
plt.title('top 10 most demanded skills in the IT Sector')
plt.ylabel('no. of Occurrences skill being is demanded in different sectors')
plt.xlabel('top 10 skills ')
plt.show()


# ### Job Distribution by Industry

# In[37]:


# Job Distribution by Industry
#Determine the number of job postings in each industry. This can help identify which industries are hiring more actively.


# In[38]:


max_job_postings = df['Industry'].value_counts().head(10)


# In[39]:


min_job_posting = df['Industry'].value_counts().tail(10)


# In[40]:


max_job_postings.plot(kind = 'bar', color = 'Grey')
plt.xlabel('Top 10 industry that offers various job Roles')
plt.ylabel('number of job Roles they offer with different skills')
plt.title('Top 10 industries that offers wide range of opportunities(Roles) to work')
plt.show()


# ### Location Analysis

# In[41]:


#Analyze the number of job postings by location (city) to see which locations have more job opportunities.


# In[42]:


df1 = pd.read_csv('Documents/encoded-Job opportunities.csv')


# In[43]:


locations = df1['Location'].value_counts()
locations.sort_index()
plt.plot(locations)
plt.plot(locations.index, locations.values, marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45, fontsize=12)  # Adjust fontsize as needed
plt.xlabel('locations')
plt.ylabel('No. of Job Opportunities')
plt.title('Locations with respect to no. of job Opportunities')
# Displaying the plot
plt.tight_layout()  # Adjust layout to ensure everything fits without overlap
plt.show()


# ### Salary Trends

# In[44]:


df.head(10)


# In[45]:


df['Average Salary'] = (df['Min Salary'] + df['Max Salary']) / 2

# Group by Job Title and calculate the mean of the average salary
average_salary = df.groupby('Job Title')['Average Salary'].mean().reset_index()


# ### top 10 average salary of each job feilds

# In[46]:


average_salary.head(10).sort_values(by ='Average Salary',ascending = False).reset_index()


# ### avg salary variation with respect to experience level

# In[47]:


avg_sal_by_explevel = pd.DataFrame(df.groupby('Experience Level')['Average Salary'].mean().reset_index())
avg_sal_by_explevel.set_index('Experience Level',inplace= True)


# In[48]:


avg_sal_by_explevel


# In[49]:


avg_sal_by_explevel.plot(kind='bar', color = 'Green')


# ### Salary Trends with respect to Industries

# In[50]:


avg_sal_indus = pd.DataFrame(df.groupby('Industry')['Average Salary'].mean().reset_index())
avg_sal_indus.set_index('Industry',inplace= True)


# In[51]:


avg_sal_indus.sort_values(by = 'Average Salary', inplace = True, ascending =False)


# In[52]:


avg_sal_indus.head(10)


# In[53]:


avg_sal_indus.tail(10)


# ### Salary Trends with respect to Required Skill

# In[54]:


df['Required Skills'].unique()


# In[55]:


skills_sal = pd.DataFrame(df.groupby('Required Skills')['Average Salary'].mean().reset_index())
skills_sal.set_index('Required Skills',inplace= True)


# In[56]:


skills_sal.head(10).sort_values(by = 'Average Salary', ascending = False)


# In[57]:


skills_sal.head(10).sort_values(by = 'Average Salary', ascending = False)


# In[83]:


explev = df['Experience Level'].value_counts()
plt.pie(explev, labels = explev.index, autopct = '%1.1f%%')
plt.title('Job opportuities with respect to Experience Level')
plt.show()


# ### Company and Industry

# #### Which companies are hiring for entry-level positions?

# In[59]:


entry_level = df[df['Experience Level']=='Entry-Level']
mid_level = df[df['Experience Level']=='Mid-Level']
senior = df[df['Experience Level']=='Senior']
junior = df[df['Experience Level']=='Junior']
intern = df[df['Experience Level']=='Internship']


# In[88]:


entry_level['Industry'].unique().tolist()


# In[61]:


print('the entry level employees are appointed for the jobs :\n\n',(entry_level['Job Title'].unique().tolist()))


# In[63]:


print('Companies those hire for entry level positions \n\n ',entry_level['Company'].unique())


# In[64]:


print('Companies those hire for Junior positions \n\n ',junior['Company'].unique())


# In[65]:


print('Companies those hire for  positions \n\n ',entry_level['Company'].unique())


# In[66]:


pd.DataFrame(entry_level['Company'].value_counts())


# In[67]:


pd.DataFrame(junior['Company'].value_counts())


# In[68]:


pd.DataFrame(mid_level['Company'].value_counts()).head(10)


# In[69]:


pd.DataFrame(senior['Company'].value_counts())


# In[70]:


pd.DataFrame(intern['Company'].value_counts())


# In[ ]:





# ### Which job title had the most recent postings?

# In[71]:


df.loc[df['Date Posted'].idxmax()]


# ## Salary Comparisons:

# ### What is the highest salary offered across all positions?

# In[72]:


df.loc[df['Max Salary'].idxmax()]


# ### How does the maximum salary for Network Engineers compare to the minimum salary for Software Engineers?

# In[73]:


se = df[df['Job Title']=='Software Engineer']['Min Salary'].max()
ne = df[df['Job Title']=='Network Engineer']['Max Salary'].max()


# In[74]:


print('\n\nThe minimum salary of Software engineer is',se,'and thus of Network engineers maximum salary is',ne,'\n ')
if(se>ne):
    print('Software engineer Minimum salary is lesser than Network engineer Maximum Salary by ',se-ne)
else:
    print('The Network engineers Maximum Salary exceeds Software Engineer Minimum salary by', ne-se )


# In[76]:


dfg = df[df['Industry']=='Cloud Computing']


# In[77]:


dfg['Job Title'].unique()


# In[ ]:




