#Read CSV into python
import os
import csv

csvpath = os.path.join('raw_data','budget_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter = ',')
    #my_list = [[int(x) for x in rec] for rec in csv.reader(p, delimiter=',')]
    next(csv_data)
#Store csv as lists
    data = list(csv_data)
    print(data)


 # change string list to int
    
#count rows to find total months and set to varialbe -1
    count_data = len(data) 
    total_months = count_data - 1  # -1 due to column header
    

#Create list for Revenue only
    revenue_list = [item[1] for item in data]
    print(revenue_list) #works
#------------------------------------------------------don't mess with above
    #Sum Revenue list set variable as Total_Revenue
    total_revenue = sum(revenue_list)
   

#What is the average revenue change



# find greatest increase in revenue.  max()
    max_increase = max(revenue_list)
    print(max_increase)
# find greated decrease in revenue. min()
    min_increase = min(revenue_list)
    print(min_increase)

#Final output
#print("Financial Analysis")
#print("------------------------------------")
#print(f"Total Months: "{total_months})
#print(f"Total_Revenue: "{})
#print(f"Average Revenue Changes: "{})
#print(f"Greatest Increase in Revenue: "{max_increase})
#print(f"Greatest Decerase in Revenue: "{})

#csvpath = os.path.join('raw_data','budget_data_1.csv')
#with open(csvpath, newline='') as csvfile:
    #csv_data = csv.reader(csvfile, delimiter = ',')