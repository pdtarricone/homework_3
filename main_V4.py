import csv
path = "/Users/tarricone/Documents/UCSD-VIRT-DATA-PT-05-2023-U-LOLC/02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv"
file = open(path, mode = "r")
reader = csv.reader(file)

#for row in reader: 
   #print(row)

header = []
header = next(reader)
# print(header)

rows = []
for row in reader: 
    rows.append(row)

file.close()

lines = []


str1="Financial Analysis"
print(str1)
lines.append(str1)

str1="-----------------------------------"
print(str1)
lines.append(str1)

total_months = len(rows)
str1 = ("Total Months:" + str(total_months))
print (str1)
lines.append(str1)

total = 0 
for row in rows: 
    total = total + int(row[1])

str1=("Total: $"+ str(total))
print(str1)
lines.append(str1)

delta = 0 
change = []
previous = []

for row in rows:
    if change != []:
        last = int(previous[1])
        current = int(row[1])
        delta = current - last 
    change.append(delta)
    previous = row

avg_change = sum(change)/(total_months-1)
avg_change_f = "{:.2f}".format(avg_change)

str1=("Average Change: ($" + str(avg_change_f)+")")
print(str1)
lines.append(str1)

max_profit = 0 
max_date = ""
previous = []

for row in rows: 
    if previous != []:
        last = int(previous[1])
        current = int(row[1])
        max_current = current - last 
        if (int(max_current) > int(max_profit)): 
            max_profit = max_current 
            max_date = row[0]
    previous = row 


str1=("Greatest Increase In Profits: "+ max_date + " ($" + str(max_profit) + ")")
print(str1)
lines.append(str1)

min_profit = 0 
min_date = ""
previous = []

for row in rows: 
    if previous != []:
        last = int(previous[1])
        current = int(row[1])
        min_current = current - last 
        if (int(min_current) < int(min_profit)): 
            min_profit = min_current 
            min_date = row[0]
    previous = row 


str1=("Greatest Decrease In Profits: "+ min_date + " ($" + str(min_profit) + ")")
print(str1)
lines.append(str1)

with open("budget_out.txt","w") as outfile: 
    for line in lines: 
        outfile.write(line)
        outfile.write("\n")
        # print(line+"\n")

### Second Part of the Assignment

import csv
path = "/Users/tarricone/Documents/UCSD-VIRT-DATA-PT-05-2023-U-LOLC/02-Homework/03-Python/Starter_Code/PyPoll/Resources/election_data.csv"
file = open(path, mode = "r")
reader = csv.reader(file)

#for row in reader: 
   #print(row)

header = []
header = next(reader)
## print(header)

rows = []
for row in reader: 
    rows.append(row)

file.close()

lines = []


str1="Election Results"
print(str1)
lines.append(str1)

str1="-----------------------------------"
print(str1)
lines.append(str1)

total_votes = len(rows)
str1 = "Total Votes: " + str(total_votes)
print(str1)
lines.append(str1)

str1="-----------------------------------"
print(str1)
lines.append(str1)

vote_dict = {}
for row in rows:
    key = row[2]

    if row[2] not in vote_dict: 
        vote_dict[key] = 1
    else: 
        vote_dict[key] = vote_dict[key]+1 

mystr = "" 
out_list=[]
percentage_list = []

for key in vote_dict: 
    percentage = (vote_dict[key]/total_votes)*100
    percentage_list.append((percentage, key))
    percentage_f = "{:.3f}".format(percentage)
    mystr = mystr + key + ": " + percentage_f + "% (" + str(vote_dict[key]) + ")"
    out_list.append(mystr)
    mystr = ""

for item in out_list:
    print(item)
    lines.append(item)

max = 0 
winner = "none"

for item in percentage_list: 
    if item[0] > max: 
        max = item[0]
        winner = item[1]

str1 = "-----------------------------------"
print(str1)
lines.append(str1)

str1 = ("Winner: " + winner)
print(str1)
lines.append(str1)

str1 = ("-----------------------------------")
print(str1)
lines.append(str1)

with open("election_out.txt","w") as outfile: 
    for line in lines: 
        outfile.write(line)
        outfile.write("\n")
        # print(line+"\n")        

