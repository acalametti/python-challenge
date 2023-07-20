
#read import necessary programs 
import os
import csv

#read in csv and creat txt file for analysis report
pybank_report = open('analysis/Report.txt','w')
pybank_data = csv.reader(open('Resources/budget_data.csv'))

#store header 
pybank_header = next(pybank_data)

#assign variables 
total = 0 
months = 0
total_change = 0
previous_rev = 0
increase = ["",0]
decrease = ["",0]

for row in pybank_data:
    # months = months + 1 (+= shortcut provided by Geronimo Perez)
    months += 1
    
    #make string into integer
    revenue = int(row[1])
    
    #the calculate the total revenue
    total = total + revenue

    #find the total change in revenue 
    change = revenue - previous_rev
    if previous_rev == 0:
        change = 0

   #add the change to the total change  
    total_change = total_change + change


    #calculte the net change in profit/loss using if statment
    if change > increase[1]:
        increase[0] = row[0]
        increase[1] = change

    if change < decrease[1]:
        decrease[0] = row[0]
        decrease[1] = change

    #make it so the the pevious revenue calculation becomes new starting point
    previous_rev = revenue


#fill in output table with variables created (Mapping :,2f shortcut provided by Geronimo Perez)
output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_change/(months-1):,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
'''
#print outputs 
print(output)
pybank_report.write(output)
