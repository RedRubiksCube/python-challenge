import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#This will turn total months into a list 
revenue = 0
def calculations (data):
    #months = str(data[0])
    #profit = int(data[1])

    #Gets total amount of rows    
    month_count = (sum(1 for row in csvreader) + 1)
    
    #Totals Monthly profit/loss
    revenue_total = sum(int(data[1]) for row in csvreader)

    #All print statements
    print(month_count) #Should be 86
    
    #Print Monthly revenue
    #print(total) #Total Profil/Loss should be 38,382,578


#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
       
    header = next(csvreader) #excludes header column
    #row = next(csvreader)
    for row in csvreader:
        P_F = calculations(row)
    
