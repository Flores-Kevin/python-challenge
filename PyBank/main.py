#PyBank Financial Analysis Script

#Importing modules
import csv
import os


#declaring dictionary
#months = {"Jan":0,"Feb":0,"Mar":0,"Apr":0,"May":0,"Jun":0,"Jul":0,"Aug":0}

#Declared variables
header = ("Financial Analysis")
dashes = "----------------------------------------"
month_counter = []
profit_loss = []
total_sum = []
change = []
Inc = []
Dec = []
avg_change = []

#Stored file path to given budget data.
file = 'Resources/budget_data.csv'

#Opened file in read mode, storing contents under variable "budget"
with open(file, "r") as budget:

#Stores contents of budget into variable: "data"
    data = csv.reader(budget, delimiter=",")

#Sets loop to iterate through list
    for i in data:
#Appends data to specific lists
        month_counter.append(i[0])
        profit_loss.append(i[1])

#takes out the header of the list which is a string. "Date/Profit-Loss"
    profit_loss.pop(0)
    month_counter.pop(0)

#changes the profit_loss[] from strings to integers
int_list = []
for i in profit_loss:
    int_list.append(int(i))

#Loops through the profit/loss list and returns a list of change from month to month
for i in range((len(month_counter)-1)):
    change.append(int_list[i]-int_list[i-1])

#calculate the average change from change list
avg_change = (sum(change)/len(month_counter))

#Loops through and finds the max and min
for i in int_list:
    Inc = max(change)
    Dec = min(change)

#f string to print total months string and counter
Months = (f"Total Months: {len(month_counter)}")
Totals = (f"Total: ${sum(int_list)}")
Avg_Chg = (f"Average change: ${avg_change}")
Prof_Inc = (f"Greatest increase in profits: ${Inc}")
Prof_Dec = (f"Greatest decrease in profits: ${Dec}")

#creating a function to print results
def Financial_Analysis():
    print(header)
    print(dashes)
    print(Months)
    print(Totals)
    print(Avg_Chg)
    print(Prof_Inc)
    print(Prof_Dec)
    print("\n")
#Calling function that prints results
Financial_Analysis()

#zips print statements
cleaned = [header,dashes,Months,Totals,Avg_Chg,Prof_Inc,Prof_Dec]
#openning the output file and writing to it
out_file = os.path.join("../analysis/anaylysis.csv")
with open(out_file, "w") as datafile:
    writer = csv.writer(datafile)
    # writer.writerow(header,Months,Totals,Avg_Chg,Prof_Inc,Prof_Dec)
    writer.writerows(cleaned)