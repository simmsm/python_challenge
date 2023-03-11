#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import dependencies 
import pandas as pd 


# In[7]:


#store file path as variable and read as csv
datafile= "election_data.csv"
datafile=pd.read_csv(datafile)


# In[88]:


#find the total number of votes cast
total_votes=datafile.shape[0]


# In[109]:


#find the number of unique canidates, create list to store values 
candidate_list=[]
candidate_list=datafile["Candidate"].unique()


# In[108]:


# find number of votes cast for each candidate, create list to store values 
num_vote=[]
num_vote=datafile["Candidate"].value_counts()

#convert into a dataframe 
num_vote_dataframe=pd.DataFrame(num_vote)


# In[95]:


#percent each candidate recieved, create list to store values 
percentage_votes= []
DeGette=(num_vote[0]/num_vote.sum()*100)
Stockham=(num_vote[1]/num_vote.sum()*100)
Doane=(num_vote[2]/num_vote.sum()*100)
percentage_votes.append("%.3f%%" %(DeGette))
percentage_votes.append("%.3f%%" %(Stockham))
percentage_votes.append("%.3f%%" %(Doane))


# In[114]:


#append percentage of votes recieved in a new column and label "Percentage Votes"
num_vote_dataframe["Percentage Votes"]=percentage_votes

#rename colum to "Votes Received"
df_renamed=num_vote_dataframe.rename(columns={"Candidate":"Votes Received"})
df_renamed


# In[119]:


#take first row name and print as winner 
winner=df_renamed.head(1).index[0]
winner


# In[123]:


print ("Total Votes: ", total_votes)
print (df_renamed)
print ()
print ("Winner: ", winner)


# In[ ]:




