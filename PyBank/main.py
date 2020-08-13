import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
       
    header = next(csvreader) #excludes header column 

    # Code below calculates the total amount revenue   
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
    

    for i in range(len(monthly_rev)):
        j = int(i - 1)
        if j > 0:
            diff = (int(monthly_rev[j]) - int(monthly_rev[i]))
            monthly_rev_diff.append(diff)
        
    avg = sum(monthly_rev_diff)/len(monthly_rev_diff)   
          

    
    
    #All prints
    print(len(tot_month))
    print(totals3)
    print(avg)