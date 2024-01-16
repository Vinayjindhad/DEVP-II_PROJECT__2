#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Objective of the Dashboard:
st.header("Objective of the Dashboard:")
st.write("The primary objective of this dashboard is to provide a comprehensive analysis of mineral production in India.")
st.write("Key focus areas include understanding the distribution of minerals, identifying prominent contributors among states,")
st.write("analyzing yearly trends, and exploring specific insights into the production of coal, lignite, natural gas, and offshore petroleum.")
st.write("The dashboard aims to facilitate informed decision-making by stakeholders involved in resource management and policymaking.")


# In[3]:


# Data Overview:
st.header("Data Overview:")
st.write("The dataset provides detailed information on mineral production in India, spanning the years 2010-11 to 2014-15(P).")
st.write("It includes key metrics such as quantity and value for various minerals, across different states.")
st.write("The dataset covers essential minerals like coal, lignite, natural gas, and petroleum.")

# Dashboard Analysis:

## 1. Mineral Distribution:
st.header("1. Mineral Distribution:")
st.write("- The dashboard highlights a diverse distribution of minerals.")
st.write("- Prominent minerals, identified based on cumulative quantities and values, play key roles in the nation's mineral wealth.")

## 2. State-wise Analysis:
st.header("2. State-wise Analysis:")
st.write("- Considerable disparities exist in mineral production across states.")
st.write("- States such as Orissa, Jharkhand, and others emerge as significant contributors, impacting the overall mineral landscape.")

## 3. Coal Production Analysis:
st.header("4. Coal Production Analysis:")
st.write("- Coal, a vital mineral, exhibits varying production patterns across states.")
st.write("- States like Jharkhand and others play pivotal roles in national coal production.")

## 4. Lignite and Natural Gas Exploration:
st.header("5. Lignite and Natural Gas Exploration:")
st.write("- Exploration of lignite and natural gas unveils specific insights.")
st.write("- Notable states, such as Gujarat and Tamil Nadu, demonstrate distinctive trends in these mineral categories.")

## 5. Offshore Petroleum Production:
st.header("6. Offshore Petroleum Production:")
st.write("- The offshore petroleum sector significantly contributes to the nation's energy resources.")
st.write("- States like Gujarat and others play key roles in offshore petroleum extraction.")

# Overall Implications:
st.header("Overall Implications:")
st.write("- The analysis aids in understanding the dynamics of mineral production in India.")
st.write("- Stakeholders can leverage these insights for strategic resource management, policy formulation, and investment decisions.")

st.write("This dashboard serves as a valuable tool for anyone interested in gaining a nuanced perspective on India's mineral production landscape.")


# In[4]:


# Load your dataset
# Replace 'your_dataset.csv' with the actual name of your dataset file
df = pd.read_csv('production.csv')


# In[5]:


# Streamlit App
st.title("Mineral Production Dashboard and Report")

# Aspect 1: Mineral Distribution
st.header("Aspect 1: Mineral Distribution")

# Visualization
mineral_distribution = df.groupby('Mineral').agg({'Quantity 2014-15(P)': 'sum', 'Value 2014-15(P)': 'sum'})
st.bar_chart(mineral_distribution)


# In[6]:


# Mineral Distribution:
st.header("Mineral Distribution:")
st.write("We observed a diverse distribution of minerals, with some contributing significantly to overall production.")
st.write("Noteworthy minerals include Coal and Petroleum based on their cumulative quantities and values.")


# In[7]:


# Aspect 2: State-wise Analysis
st.header("Aspect 2: State-wise Analysis")

# Visualization
state_analysis = df.groupby('States').agg({'Quantity 2014-15(P)': 'sum', 'Value 2014-15(P)': 'sum'})
st.bar_chart(state_analysis)


# In[8]:


# State-wise Analysis:
st.header("State-wise Analysis:")
st.write("States exhibit considerable disparities in mineral production, both in terms of quantity and value.")
st.write("States such as Orissa,Rajasthan emerge as prominent contributors to the nation's mineral wealth.")


# In[9]:


# Aspect 3: Coal Production Analysis
st.header("Aspect 3: Coal Production Analysis")

# Visualization
coal_production = df[df['Mineral'] == 'Coal'].groupby('States').agg({'Quantity 2014-15(P)': 'sum', 'Value 2014-15(P)': 'sum'})
st.bar_chart(coal_production)


# In[10]:


# Coal Production Analysis:
st.header("Coal Production Analysis:")
st.write("Coal, a vital mineral, showcased varying production patterns across states.")
st.write("States like Jharkhand,orissa played pivotal roles in national coal production.")


# In[11]:


# Aspect 4: Lignite and Natural Gas Exploration
st.header("Aspect 4: Lignite and Natural Gas Exploration")

# Visualization
lignite_gas = df[df['Mineral'].isin(['Lignite', 'Natural Gas (ut.)'])]
sns.catplot(x='Mineral', y='Quantity 2014-15(P)', hue='States', data=lignite_gas, kind='bar')
st.pyplot(plt.gcf())


# In[12]:


# Lignite and Natural Gas Exploration:
st.header("Lignite and Natural Gas Exploration:")
st.write("Exploration of lignite and natural gas revealed [specific insights].")
st.write("Notable states such as Tamil Nadu demonstrated distinctive trends in these mineral categories.")


# In[13]:


# Aspect 5: Offshore Petroleum Production
st.header("Aspect 5: Offshore Petroleum Production")

# Visualization
offshore_petroleum = df[df['Mineral'] == 'Petroleum(crude)'].groupby('States').agg({'Quantity 2014-15(P)': 'sum', 'Value 2014-15(P)': 'sum'})
st.bar_chart(offshore_petroleum)


# In[14]:


# Offshore Petroleum Production:
st.header("Offshore Petroleum Production:")
st.write("The offshore petroleum sector contributed significantly to the nation's energy resources.")
st.write("States such as Rajasthan played key roles in offshore petroleum extraction.")


# In[ ]:





# In[ ]:




