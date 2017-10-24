#Read CSV into python
import os
import csv

                    #csvpath = os.path.join('raw_data','budget_data_1.csv')
                    #with open(csvpath, newline='') as csvfile:
                    #csv_data = csv.DictReader(csvfile, delimiter = ',')
 

 with open('raw_data','budget_data_1.csv') as cvsfile:
    cvsreader = csv.DictReader(cvsfile)

    for row in reader:
        print(row["Revenue"], row["Date"])

#Store csv as lists
    data = list(csv_data) 
    print(data)
#count rows to find total months and set to varialbe -1
    count_data = len(data) 
    total_months = count_data - 1  # -1 due to column header
    

#Create list for Revenue only
for row in data:
    revenue_list = data[1]
    print(revenue_list)
    #Sum Revenue list set variable as Total_Revenue

#What is the average revenue change



# find greatest increase in revenue.  max()
#max_increase = max(data)
#print(max_increase)
# find greated decrease in revenue. min()
#min_increase = min(data)
#print(min_increase)

#Final output
#print("Financial Analysis")
#print("------------------------------------")
#print(f"Total Months: "{total_months})
#print(f"Total_Revenue: "{})
#print(f"Average Revenue Changes: "{})
#print(f"Greatest Increase in Revenue: "{max_increase})
#print(f"Greatest Decerase in Revenue: "{})