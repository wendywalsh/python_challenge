#Read CSV into python
import os
import csv

csvpath = os.path.join('raw_data','budget_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter = ',')
    data = list(csv_data)
    count_data = len(data)
    print(csv_data)
    print(count_data - 1) # -1 due to column header
#Print rows as lists
   

#Create list for Date index 0 


    #save as "Total_Months"
    #print lenth of list for Date 

#Create list for Revenue
    
    #Sum Revenue list set variable as Total_Revenue

#What is the average revenue change



# find greatest increase in revenue.  max()


# find greated decrease in revenue. min()