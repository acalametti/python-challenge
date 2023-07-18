import csv
my_report = open('analysis/Report.txt','w')
data = csv.reader(open('Resources/budget_data.csv'))

next(data)

total = 0 
months = 0
total_change = 0
pre_rev = 0
inc = ["",0]
dec = ["",0]

for row in data:
    # months = months + 1
    months += 1
    
    #make string into integer
    rev = int(row[1])
    
    #the total 
    total += rev

    change = rev - pre_rev
    if pre_rev == 0:
        change = 0
    
    total_change += change

    if change > inc[1]:
        inc[0] = row[0]
        inc[1] = change

    if change < dec[1]:
        dec[0] = row[0]
        dec[1] = change


    pre_rev = rev

output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_change/(months-1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]:,})
Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})
'''

print(output)
my_report.write(output)
