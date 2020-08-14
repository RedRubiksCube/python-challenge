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
total_months_str = str(len(tot_month))   

#finds max and min and saves as string
maximum_prof_change = str(max(monthly_rev_diff))
minimum_prof_change = str(min(monthly_rev_diff))

#All prints
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + total_months_str)
print("Total: $" + str(totals3))
print("Average change: $" + str(average_month_revenue))
print("Greatest Increase in Profits: $" + maximum_prof_change)
print("Greatest Decrease in Profits: $" + minimum_prof_change)


#All writing to txt file   
Analysis = open('Analysis/Financial_Analysis.txt', "w")
Analysis.write("Financial Analysis"  + '\n')
Analysis.write("-------------------------------"  + '\n')
Analysis.write("Total Months: " + total_months_str  + '\n')
Analysis.write("Total: $" + str(totals3)  + '\n')
Analysis.write("Average change: $" + str(average_month_revenue)  + '\n' )
Analysis.write("Greatest Increase in Profits: $" + maximum_prof_change  + '\n')
Analysis.write("Greatest Decrease in Profits: $" + minimum_prof_change  + '\n')