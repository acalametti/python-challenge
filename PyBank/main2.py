'Start by reading in the CSV '
import os
import csv
import pandas as pd
'use the file path to import csv file '
budget_csv = os.path.join('PyBank','Resources','budget_data.csv')

'Open CSV data'
with open(budget_csv) as csvfile:
    csvreader_pybank = csv.reader(csvfile, delimiter = ',')
    print(csvreader_pybank)

    'store header rows '
    csv_pybank_header = next(csvreader_pybank)

    print(f"CSV Header: {csv_pybank_header}")

    'am I supposed to be usign pandas or just normal python commands?'

    'read the rows of data'
    for row in csvreader_pybank:
        print(row)


'bring in pandas reader'
pybank_df = pd.read_csv(budget_csv)
print(pybank_df.head())
df = pd.DataFrame(pybank_df)

'find the total number of months'

'find the net total amount of profit/loss'
'calculate average change in profit/loss over period'
total_amount = df['Profit/Losses'].sum()
print(total_amount)


'average is supposed to be negative????'
average_amount = df['Profit/Losses'].mean()
print(average_amount)


'find the greatest increase in profits (date/amount)'
max_value = pybank_df.max(axis = 0)
print(max_value)
'how do you get it to calculate from one row to the next to calculate net change'

'find greatest decrease in profits (date/amount)'


"create table for financial analysis"


'print results to terminal and export as txt file'

''