import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#This will turn total months into a list 
def calculations (data):
    months = str(data[0])
    profit = int(data[1])

    #Gets total amount of rows    
    month_count = (sum(1 for row in csvreader) + 1)
    
    #Totals Monthly profit/loss
    #revenue_total = sum(float(profit))

    #All print statements
    print(month_count) #Should be 86
    
    #Print Monthly revenue
    #print(reveune_total) #Total Profil/Loss should be 38,382,578


#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
       
    header = next(csvreader) #excludes header column
    
    #######
    #I know the code below works for sure - with accurate data
    csvdata = list(csvreader)
    row_count = len(csvdata)
    print(row_count)
    #######
    
    # Code below calculates the total amount revenue   
    monthly_rev = [] 
    for row in csvreader:
        values = row[1] 
        monthly_rev.append(values)          
    monthly_rev_list = [float(integral) for integral in monthly_rev] 
    totals3 = sum(monthly_rev_list) 
    
    #print(totals3)
    #for row in csvreader:
    #    calculations(row)
    
