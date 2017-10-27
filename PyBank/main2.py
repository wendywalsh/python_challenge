#Read CSV into python
import os
import csv

csvpath = os.path.join('raw_data','budget_data_1.csv')
with open(csvpath) as csvfile:
    reader= csv.DictReader(csvfile)
    


#Declare variables
    total_months = 0
    total_revenue = 0
    date_for_increase = "unkown"
    max_decrease = 0
    max_increase = 0
    date_for_decrease = "unkown"
    delta = 0
    average_delta = 0
    previous_month_rev = 0
    current_month_rev = 0
    Avg_change = 0



# create loop 
    for row in reader:
        previous_month_rev = current_month_rev # set total as iterates through rows
  #get count total rows for total months      
        total_months = total_months + 1
  # get total revenue
        total_revenue = total_revenue + int(row["Revenue"])
    #print(total_revenue)
        if previous_month_rev == 0:
            skip = int(row["Revenue"])  # first row has no previous

    # set current month value
        current_month_rev = int(row["Revenue"])
    
    # find difference between months
        change = current_month_rev - previous_month_rev
    
    # Sum monthly changes
        delta = delta + change 
       
    # find max and min changes

        if change > max_increase:
            max_increase = change
            max_increase_date = row["Date"]
        elif change < max_decrease:
            max_decrease = change
            max_decrease_date = row["Date"]

    Avg_change = delta - skip
    avg_diff= Avg_change/(total_months -1)


#Final output
    print("Financial Analysis")
    print("------------------------------------")

    print("total_months:" + str(total_months))
    print("total revenue:" + str(total_revenue))
    print("average change:" + str(avg_diff))
    print("max increase:" + str(max_increase))
    print("max increase:" + str(max_increase_date))
    print("max decrease:" + str(max_decrease))
    print("max decrease date" + str(max_decrease_date))


  





 



