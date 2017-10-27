#Read CSV into python
import os
import csv

csvpath = os.path.join('raw_data','budget_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter = ',')
    #my_list = [[int(x) for x in rec] for rec in csv.reader(p, delimiter=',')]
    next(csv_data)

    data = list(csv_data)
    total_months= len(data) 
    print(total_months)  

#count rows to find total months and set to varialbe -1
    

# change revenue data to integer
    for row in csv_data: 
        revenue_data = int(row[1])
        
    revenue_list = list(revenue_data)   
    print(revenue_list)

#data = list(csv_data)
#total_months= len(data) 
#print(total_months)  
     
   
#Create list for Revenue only
    #revenue_list = [item[1] for item in data]
    #print(revenue_list) #works
#------------------------------------------------------don't mess with above
    #Sum Revenue list set variable as Total_Revenue
    #total_revenue = sum(revenue_data)
    #print(revenue_data)
   

#What is the average revenue change



# find greatest increase in revenue.  max()
    #max_increase = max(revenue_list)
    #print(max_increase)
# find greated decrease in revenue. min()
    #min_increase = min(revenue_list)
    #print(min_increase)

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