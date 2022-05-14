#Pypoll Election Data Analysis

###############################
#Importing dependencies
import csv
import os
from collections import Counter

###################################################
#Declaring Variables and some strings to be printed
ID = []
County = []
Candidate = []
Vote_Sum = 0
Winner = 0
Data_Header = "Election Results"
Dashes = "-----------------------------------------"
Name1 = "Charles Casper Stockham"
Name2 = "Diana DeGette"
Name3 = "Raymon Anthony Doane"

###################################################################################
#Writing file path to read, read, and creates a for loop to append columns to lists
file = "Resources/election_data.csv"
with open(file,'r') as election:
    data = csv.reader(election,delimiter = ",")
    for i in data:
        ID.append(i[0])
        County.append(i[1])
        Candidate.append(i[2])

#############################################################################################################
#After header has been successfully stored this removes the header rows for the ID[] County[] and Candidate[]
ID.pop(0)
County.pop(0)
Candidate.pop(0)

#################################################
#Makes a dictionary counting votes for candidates
Vote_Counter = Counter(Candidate)

#########################################################################
#Sums the number of votes and creates rounded percentages for those votes
V1 = (Vote_Counter[Name1])
V2 = (Vote_Counter[Name2])
V3 = (Vote_Counter[Name3])
Vote_Sum = (V1+V2+V3)
Per1 = round((float((V1/Vote_Sum)* 100)),3)
Per2 = round((float((V2/Vote_Sum)* 100)),3)
Per3 = round((float((V3/Vote_Sum)* 100)),3)

####################
#Declares the winner
if V1 > V2:
    Winner = Name1
elif V2 > V3:
    Winner = Name2
else:
    Winner = Name3

########################################
#f strings to call during print function
Ttl_Votes = (f"Total votes: {Vote_Sum}")
Win = (f"Winner: {Winner}")
C1 = (f"{Name1}: {Per1}%  ({V1})")
C2 = (f"{Name2}: {Per2}%  ({V2})")
C3 = (f"{Name3}: {Per3}%  ({V3})")

########################
#Terminal print function
def Election_Analysis():
    print("\n")
    print(Data_Header)
    print(Dashes)
    print(Ttl_Votes)
    print(Dashes)
    print(C1)
    print(C2)
    print(C3)
    print(Dashes)
    print(Win)
    print(Dashes)
    print("\n")

########################
#Calls function to print
Election_Analysis()

#################################################
#Makes a list to iterate through for the out_file
out_print = [Data_Header,Dashes,Ttl_Votes,Dashes,C1,C2,C3,Dashes,Win,Dashes]

###############################################################################
#Declares a path and makes a file to output results to and writes results to it
out_file = os.path.join("analysis/analysis.csv")
with open(out_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(out_print)