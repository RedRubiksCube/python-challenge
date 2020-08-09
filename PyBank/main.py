import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")


totalRows = []

with open(csvpath, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Below prints the total amount of rows, subtracting one to account for the header
    totalRow = len(list(csvreader))
    print(int(totalRow) - 1) 
#Total loss = -7327426
#Total Profit = 45710004
