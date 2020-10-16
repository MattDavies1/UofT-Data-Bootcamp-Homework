# Import dependancies
import os
import csv
from statistics import mean

# Set filepath
csv_filepath = os.path.join("Resources", "budget_data.csv")

# establish variables
total_months = 0
net_profit = 0
average_change = []
profit_months = []
profit_values = []

# Open csv
with open(csv_filepath) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_file)                 # skip header
    for row in csv_reader:
        total_months += 1                   # The total number of months included in the dataset
        net_profit += int(row[1])           # The net total amount of "Profit/Losses" over the entire period
        
        profit_months.append(row[0])        # populate lists for min/max/delta values
        profit_values.append(int(row[1]))

# Calculate month-to-month differences
for i in range(1, len(profit_months)):
    average_change.append(profit_values[i] - profit_values[i - 1])

# Results in f-string
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit}
Average  Change: ${mean(average_change):.2f}
Greatest Increase in Profits: {profit_months[profit_values.index(max(profit_values))]} (${max(profit_values)})
Greatest Decrease in Profits: {profit_months[profit_values.index(min(profit_values))]} (${min(profit_values)})"""

# Print outputs
print(output)

# Write outputs to .txt
with open("Output.txt", 'w') as text_file:
    text_file.write(output)
