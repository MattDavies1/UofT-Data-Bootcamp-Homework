# Import dependancies
import os
import csv
from statistics import mean

# Set filepath
csv_filepath = os.path.join("Resources", "budget_data.csv")

# Establish variables
total_months = 0
net_profit = 0
average_change = []
profit_months = []
profit_values = []

# Open csv
with open(csv_filepath) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_file)                 # Skip header
    for row in csv_reader:
        total_months += 1                   # Calculate total number of months included in the dataset
        net_profit += int(row[1])           # Calculate net total amount of "Profit/Losses" over the entire period
        
        profit_months.append(row[0])        # Populate lists for min/max/delta values
        profit_values.append(int(row[1]))

# Calculate month-to-month differences
for i in range(1, len(profit_months)):
    average_change.append(profit_values[i] - profit_values[i - 1])

# Format results to f-string
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit}
Average  Change: ${mean(average_change):.2f}
Greatest Increase in Profits: {profit_months[average_change.index(max(average_change))+1]} (${max(average_change)})
Greatest Decrease in Profits: {profit_months[average_change.index(min(average_change))+1]} (${min(average_change)})"""

# Print outputs
print(output)

# Write outputs to .txt
with open("Output.txt", 'w') as text_file:
    text_file.write(output)
