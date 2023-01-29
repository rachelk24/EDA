#!/usr/bin/env python
# coding: utf-8

# ![Olympic_rings_without_rims.svg.png](attachment:Olympic_rings_without_rims.svg.png)

# # SUMMER OLYMPICS

# # **TABLE OF CONTENT**
# 
# ### 1. INTRODUCTION
# ### 2. PROBLEM STATEMENT
# ### 3. IMPORTING LIBRARIES
# 
# ### 4. Data Acquisition and Description
# ### 5. Data Pre-profiling
# ### 6. Data Pre-processing
# ### 7. Data Post-profiling
# ### 8. Exploratory Data Analysis
# ### 9. Summarization
# #### 9.1 Conclusion
# #### 9.2 Actionable Insight
# 
# # INTRODUCTION
# 
# #### The Summer Olympic Games (French: Jeux olympiques d'été), also known as the Games of the Olympiad, and often referred to as the Summer Olympics, is a major international multi-sport event normally held once every four years. The inaugural Games took place in 1896 in Athens, Greece. The tradition of awarding medals began in 1904; in each Olympic event, gold medals are awarded for first place, silver medals for second place, and bronze medals for third place.The Summer Olympics have increased in scope from a 42-event competition programme in 1896 with fewer than 250 male competitors from 14 different nations, to 339 events in 2021 with 11,420 competitors (almost half of whom were women) from 206 nations. 
# #### There has been a total of 42 sports, spanning 55 disciplines, included in the Olympic programme at one point or another in the history of the Games. The 2012 Games featured 26 sports because of the removal of baseball and softball. 
# #### With the available dataset on summer olympics we will do a descriptive study and analysis on the progress and drawbacks made since the year 1896 till 2012. 
# 
# 
# 
# 
# ## 2. PROBLEM STATEMENT
# ### 1. High growth rate of participating countries
# ####     *One of the problems that Organizers of Olympics are facing with is significant growth rate of participating countries.
# ####     *The first period of Olympic Games was held in Athens in 1896 while just 280 athletes from 13 countries were participated in      that period. In the eleventh period of Olympics in 1963 in Berlin, the number of countries that participating in the Games arrived to 4076 athletes. 
# ####    * On the other hand today the participation of women has increased in all areas of sport and now we are seeing many competitions of women in various courses.
# ####     *So the high cost of supports and large corporations is needed. To this, National Olympic Committee is dependent to be       supporting by International Companies and also to TV broadcasting rights.
# 
# ### 2. Seeking superiority of governments
# ####     *In the most of Olympics, the U.S. based on planned programs will gain the highest medals of these Games and is located in the first place in medal ranking table of Olympics periods. After the Soviet collapse, the U.S. continues its lone greyhound in the sport like other areas and thus seeks superiority and its consolidation.
# 
# ### 3. Victory and participation in Games
# ####     *Olympics Games has the high degree of credibility in sight of millions of viewers. Therefore participation in these Games is so important for all participating countries.
# ####     *The IOC aim was based on presence of participant's countries in these tournaments and was not based on their victories.
# 
# ### 4. Number of sports events
# ####     *The first period of the Olympic Games that held in Athens in 1896 had 9 sports and 43 events. In the third period of Olympic Games in 1904 in Switzerland, the number of events had reached 85 events that had one hundred percent growth rate.
# ####     *Olympic Movement experts states that increasing the sports in program of Olympic is one of the serious threats for Olympic Movement.
# 
# ### 5. Economics of Hosting the Olympic Games
# ####     *The costs of hosting the Olympics have skyrocketed. This has led to fewer states interested in playing host and a search for options to lighten the burdens of staging the big event.
# ####     *A growing number of economists say that it leaves many host countries with large debts and maintenance liabilities. 
# 
# 

# ## 3.  IMPORTING LIBRARIES

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# ## 4. DATA ACQUISITION AND DESCRIPTION

# In[4]:


data = pd.read_csv('https://raw.githubusercontent.com/insaid2018/Term-1/master/Data/Projects/summer%20olympics.csv')


# In[7]:


data


# In[8]:


data.info()


# In[9]:


data.nunique()


# In[10]:


data.count()


# In[11]:


data.shape


# In[12]:


data['Sport'].unique()


# In[13]:


data.dtypes


# In[14]:


data.columns


# In[15]:


data.describe()


# ## 5. DATA PRE-PROFILING

# In[16]:


data.describe()


# In[17]:


data.Year.value_counts()


# In[18]:


data.City.value_counts()


# In[19]:


data.Sport.value_counts()


# In[20]:


data.Discipline.value_counts()


# In[21]:


data.Athlete.value_counts()


# In[22]:


data.Country.value_counts()


# In[23]:


data.Gender.value_counts()


# In[26]:


data.groupby('Gender').get_group('Women')


# In[24]:


data.Event.value_counts()


# In[25]:


data.Medal.value_counts()


# In[27]:


data.isnull().sum()


# #### There are 4 null values in the 'Country' column

# In[28]:


data.notnull().sum()


# #### If we recheck, there are  31161 values in Country column and all other columns have 31165 values.

# In[29]:


bool_series = pd.isnull(data["Country"])
data[bool_series]


# In[30]:


data.groupby('Athlete').get_group('Pending')


# ## 5. DATA PRE-PROCESSING

# In[31]:


data.loc[31110,["Country"]] = 'RUS'
data.loc[31110]


# #### The missing value in row no. 31110, in the column country was filled with the country "RUS" since the Athlete Besik Kudukhov played for Russia

# In[32]:


rows =[29603, 31072,31091]
data.drop(index = rows)


# #### The rows which were having null values and even the athletes names were not mentioned are removed

# In[33]:


rows =[29603, 31072,31091]
data.drop(index = rows, inplace = True)


# In[34]:


data.shape


# In[35]:


data = data.reset_index()
print(data)


# #### The index no. are reset after removing three rows

# In[36]:


data.tail()


# In[37]:


del data['index']


# #### The previous index no. column is deleted and replaced with the new index no.

# ## 7. DATA POST-PROFILING

# In[38]:


data.head(10)


# In[39]:


data.tail(10)


# ## 8. EXPLORATORY DATA ANALYSIS

# #### QUES 1. Which are the top 10 countries that had highest participation?

# In[40]:


max = data["Country"].value_counts()[:10]
max.plot(kind = 'bar',figsize =(10,5))
plt.title('Highest Participated Country')
plt.xlabel('Countries')
plt.ylabel('number of Participation')
plt.show()


# #### QUES 2. Find the number of medals.

# In[41]:


max = data["Medal"].value_counts()
max.plot(kind = 'bar',figsize =(7,5))
plt.title('Number of  medals')
plt.xlabel('Number of Medal')
plt.ylabel('number of Participation')
plt.show()


# In[13]:


plt.figure(figsize=(20,7))
data =[10486, 10369, 10310]
Medal = ['Gold', 'Bronze', 'Silver']
plt.pie(data,labels= Medal, autopct='%1.1f%%',startangle =90)
plt.title('Number of Medals')
plt.show()


# #### QUES 3. How many men participated compared to women?

# In[42]:


plt.figure(figsize=(7,5))
sns.countplot(x='Gender',data=data)
plt.title('Number of  Men-Women participation')
plt.xlabel('Gender')
plt.ylabel('number of Participation')
plt.show()


# #### QUES 4. How many medals were won by men compared to women?

# In[43]:


sns.countplot(x='Gender',hue='Medal',data=data)
plt.show()


# #### QUES 5. Which are the 10 disciplines in which the participation was highest?

# In[44]:


max = data["Discipline"].value_counts()[:10]
max.plot(kind = 'bar',figsize =(10,5))
plt.title('Maximum disciplines')
plt.xlabel('Discipline')
plt.ylabel('number of Participation')
plt.show()


# #### QUES 6. Find the number of participations yearwise.

# In[48]:


max = data["Year"].value_counts()[:30]
max.plot(kind = 'bar',figsize =(10,5))
plt.title('Yearwise Participation')
plt.xlabel('Participants')
plt.ylabel('Year')
plt.show()


# #### Ques 7: Find the number of medals given in each year.

# In[11]:


paper = plt.figure(figsize =[17,5])
sns.countplot(x='Year',hue='Medal',data=data)
plt.show()


# #### Ques:8 Which city/country has hosted the most number of times?

# In[23]:


paper = plt.figure(figsize =[17,5])
sns.countplot(x='City',data=data)
plt.xticks(rotation = 90)
plt.show()


# #### Ques 9: What are the number of participation of men and women yearwise?

# In[40]:


paper = plt.figure(figsize =[17,5])
sns.countplot(x='Gender',hue='Year',data=data)
plt.show()


# In[49]:


data.loc[data['Year']== 1896]


# In[50]:


data.loc[data['Year']== 2008]


# ## 9. SUMMARIZATION

# ### 9.1 Conclusion
# #### From the graph it can be visualized that the U.S. has been on the top in the list of highest participation followed by Soviet Union, UK, France, Germany and Italy. After entering the former Soviet Union Countries to International sports competitions, always competitions between these two countries were very close and intensive. The tough competition between these two countries are clearly visible through the bar graph plotted.
# #### It could be seen that the medals - gold,silver and bronze were approximately equally given to the winners. In the initial years the number participants were less. Thus, the number of medals were also less. However, in each passing years as the participation increased, the number of medals has also increased. This is  one of the reason for the increase of costs in Olympic Games in recent years.
# #### The number of participation were less in the initial years for both men and women. In the year 1896 there were very less men's participation whereas there were zero women participation. In later years we can see the number of participation has increased for both men and women. In 1896, there were just 151 participation that were held whereas in the year 2008, 2042 participations were there.
# #### It can be visualized that athletics,rowing and swimming has  the highest number of participation.
# #### London is the city which has hosted Summer Olympics most number of times, followed by Athens and Los Angeles. Hosting the games is even more costly than the bidding process.
# 

# ### 9.2 Actionable Insights

# #### The Olympic Charter specifies that:"The goal of Olympism is to place sport at the service of the harmonious development of humankind,with a view to promoting a peaceful society concerned with the preservation of human dignity." In other words the unifying power of the Olympic games is to bring the world together in peaceful competition.
# 
# #### *The IOC should have a check on the high growth rate of participating countries. There should be specific limit in the entry per country in the competition.
# 
# #### *The objective of the Olympic Games is to unite all the countries of the world and to spread peace. It should be made sure that the competitions are heald in a healthy and good sportsman spirit. After entering the former Soviet Union countries in 1950 to international sports competitions,always competitions between these two countries were very close and intensive. These two countries that were seeking superiority and domination in the fields of economics, politics, military and etc. and this thought had transferred to their sports, therefore to achieve the victory they were using any tools. IOC should have a check on these.
# 
# #### *Initially the International Olympic Commiittee aim was based on presence of participant's countries in these tournaments and was not based on their victories. When Coubertin founded the modern Olympics, his goal was to pay attention to this issue that:"Important concept of Olympic is participating and victories or failures are not so important." At present the success is measured by number and color of medals and not by participation in the tournament. Increasing number of medals increases the costs. The IOC should do ammendment in the success goals, so that unnecessary costs can be cut down.
# 
# #### *Number of new sports and events has had an ascending trend. This means that in addition to increasing the number of sports, also its events were added to the program of Olympics. As stated by Olympic Movement Experts that increasing sports in Olympics is a serious threat. This can be eliminated by removing few events and by decreasing the number of sports in the Olympic Games keeping in mind the objectives of the Olympics.
# 
# #### *The Olympics are a financial drain on host cities. The Olympics force host cities to create expensive infrastructure and buildings that fall into disuse. The Olympics displace and burden residents of the host country and city. The IOC should come up with a plan regarding the hosting countries. There should be proper checklist for selecting the host nation. There shouldnt be a city that is hosting repeatedly cutting short thr burden on them.
