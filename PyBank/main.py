import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
       
    header = next(csvreader) #excludes header column 

    #All lists needed for the calculations
    monthly_rev = []
    monthly_rev_diff = [] 
    tot_month = []
    month_change_average = []
    
    for row in csvreader:
        values = row[1] 
        months = row[0]
        monthly_rev.append(values)
        
        tot_month.append(months)          
    
    #The two lines below this get the total revenue for the given period
    #They reference the monthly_rev list 
    monthly_rev_list = [float(integral) for integral in monthly_rev] 
    totals3 = sum(monthly_rev_list) 
    
    #This creates the list of the average monthly revenue but is missing the first value that is needed
    for i in range(len(monthly_rev)):
        j = int(i - 1)
        if j > -1:
            diff = (int(monthly_rev[i]) - int(monthly_rev[j]))
            monthly_rev_diff.append(diff)
        
    #this successfully finds the average change in profit
    avg = sum(monthly_rev_diff)/len(monthly_rev_diff)   
    average_month_revenue = str(round(avg, 2))     
        
    #All prints
    print(len(tot_month))
    print(totals3)
    print(average_month_revenue)
    print("Greatest Increase in Profits: $", max(monthly_rev_diff))
    print("Greatest Decrease in Profits: $", min(monthly_rev_diff))
   