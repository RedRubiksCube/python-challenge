import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

totalProfit_Loss = 0

def analyze():
    totalRow = len(list(csvreader))
    
    
    #profit = 0 
    #profit += int(row[1])
    
    #Below prints the total amount of rows, subtracting one to account for the header
    print(int(totalRow))
    #Total Profil/Loss should be 38,382,578
    #print(profit)




#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #for some reason this fails when I have two for loops, but when I combine them it will only print
    #the first row and the total amount of months or every row and no total
    for row in csvreader:
        print(row)
        
    for row in csvreader:
        analyze()
    
    
