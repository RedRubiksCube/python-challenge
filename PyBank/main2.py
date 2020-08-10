import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

totalProfit_Loss = 0

#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    header = next(csvreader) #excludes header column
    
    Profit = sum(int(row[1]) for row in csvreader) 

    for row in csvreader:
        #print(row)
        print(len(list(csvreader)))
        #Profit += int(row[1])
    print(Profit)
        
    