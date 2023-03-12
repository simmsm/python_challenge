#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


# In[135]:


#Import dependencies
import os
import csv
csvpath = os.path.join('..', "/Users/MitchSimms/Desktop/Data_Analytics/mygithub/module_3_challenge/python_challenge/PyBank/Resources/budget_data.csv")

#empty lists to store
date=[]
monthly_changes=[]
profit=[]
#second profit list will skip the first value in list 
profit_2=[]

#open csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # append date into list 
        date.append(row[0])
        
        # Append the profit into list and profit_2 list 
        profit.append(row[1])
        profit_2.append(row[1])
        
    #convert both profit lists into int
    profit = [int(i) for i in profit]
    profit_2= [int(i)for i in profit_2]
    
    #find total profits before changing the lists 
    total_profit= sum(profit)
    
    #remove first value in profit_2 list, remove last value in profit list so both are the same length 
    profit_2.pop(0)
    profit.pop(len(profit)-1)

    #create for loop to add each value from both profit lists to get the change in value for each month 
    for i in range(len(profit)):
        monthly_change= (profit_2[i])-(profit[i])
        
        #append monthly change values into list 
        monthly_changes.append(monthly_change)
        
    # average change is the sum of each month divided by the number of months      
    average_change= (sum(monthly_changes))/len(monthly_changes)
    
    #greatest increase and decrease is the min and max value of monthly changes 
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)
   
    # date of min and max values is the date list indexed to the index of max and min values
    increase_date = date[monthly_changes.index(greatest_increase_profits)+1]
    decrease_date = date[monthly_changes.index(greatest_decrease_profits)+1]  
    
    print ("Financial Analysis:")
    print ("- - - - - - - - - - - - - - - -")
    print ("Number of Months: ", len(date))
    print ("Total: ", total_profit)
    print ("Average Change: ", ("{:.2f}".format(average_change)))
    print ("Greatest Increase in Profits:",(greatest_increase_profits), " Date: ",(increase_date))
    print ("Greatest Decrease in Profits:",(greatest_decrease_profits), " Date: ",(decrease_date))
  


# In[ ]:




