import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#Loop that goes through each row of data in the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
       
    header = next(csvreader) #excludes header column 

    #All lists needed for the calculations
    Voter_ID_List = []
    County_List = []
    Candidate_List = []
    
    for row in csvreader:
        Voter_ID = row[0]
        County = row[1] 
        Candidate = row[2] 
        Voter_ID_List.append(Voter_ID)
        County_List.append(County)
        Candidate_List.append(Candidate)

#Candidate Counts
Tot_Voter_Count = int(len(Voter_ID_List))     
Khan_Count = Candidate_List.count('Khan')
Correy_Count = Candidate_List.count('Correy')
Li_Count = Candidate_List.count('Li')
Otooley_Count = Candidate_List.count("O'Tooley")

#Candidates Percentages
Khan_Percentage = (Khan_Count / Tot_Voter_Count) * 100
Correy_Percentage = (Correy_Count / Tot_Voter_Count) * 100
Li_Percentage = (Li_Count / Tot_Voter_Count) * 100
Otooley_Percentage = (Otooley_Count / Tot_Voter_Count) * 100


#Desired data as strings
#Counts
Voter_Count = str(len(Voter_ID_List))
Khan_Count_Str = str(Khan_Count)
Correy_Count_Str = str(Correy_Count)
Li_Count_Str = str(Li_Count)
Otooley_Count_Str = str(Otooley_Count)

#Percentages as strings
Khan_Percentage_Str = str(round(Khan_Percentage, 3))
Correy_Percentage_Str = str(round(Correy_Percentage, 3))
Li_Percentage_Str = str(round(Li_Percentage, 3))
Otooley_Percentage_Str =str(round(Otooley_Percentage, 3))

#Finding the winner
winner = {}
winner["Khan"] = Khan_Count
winner["Correy"] = Correy_Count
winner["Li"] = Li_Count 
winner["Otooley"] =  Otooley_Count

winner_name = max(winner, key=winner.get)

#All print statements
print("Election Results")
print("-------------------------------")
print("Total Votes: " + Voter_Count)
print("-------------------------------")
print("Khan: " + Khan_Percentage_Str + "% (" + Khan_Count_Str + ")")
print("Correy: " + Correy_Percentage_Str +  "% (" + Correy_Count_Str + ")")
print("Li: " + Li_Percentage_Str + "% (" + Li_Count_Str + ")")
print("O'Tooley: " + Otooley_Percentage_Str + "% (" + Otooley_Count_Str + ")")
print("-------------------------------")
print("Winner: " + winner_name)
print("-------------------------------")

#All writing to txt file   
Results = open('Analysis/Election_Results.txt', "w")
Results.write("Election Results"  + '\n')
Results.write("-------------------------------"  + '\n')
Results.write("Total Votes: " + Voter_Count  + '\n')
Results.write("-------------------------------"  + '\n')
Results.write("Khan: " + Khan_Percentage_Str + "% (" + Khan_Count_Str + ")" + '\n')
Results.write("Correy: " + Correy_Percentage_Str +  "% (" + Correy_Count_Str + ")" + '\n')
Results.write("Li: " + Li_Percentage_Str + "% (" + Li_Count_Str + ")" + '\n')
Results.write("O'Tooley: " + Otooley_Percentage_Str + "% (" + Otooley_Count_Str + ")" + '\n')
Results.write("-------------------------------" + '\n')
Results.write("Winner: " + winner_name +'\n')
Results.write("-------------------------------" )