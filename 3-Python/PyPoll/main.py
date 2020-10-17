# Import dependancies
import csv
import os

# Set filepath
data_path = os.path.join("Resources", "election_data.csv")

# Establish variables for reading loop
vote_total = 0
candidate_list = []

# Open file, read by line and output total number votes & list of candidates
with open(data_path, 'r', newline = '') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    header = next(csvreader)                    # Skip header
    for row in csvreader:
        vote_total += 1                         # Calculate total number of votes cast
        if row[2] not in candidate_list:
            candidate_list.append(row[2])       # Generate list of candidates who received votes

# Make Dictionary to tally votes into by candidate
vote_tally = dict.fromkeys(candidate_list , 0)

# Tally total number of votes each candidate won
with open(data_path, 'r', newline = '') as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ',')
    header = next(csvreader)                    # skip header
    for row in csvreader:
        for key in vote_tally:
            if row[2] == key:
                vote_tally[key] += 1

# Calculate percentage of votes each candidate won & put values into new dictionary
vote_pct = dict.fromkeys(candidate_list , 0)
for key in vote_pct:
    vote_pct[key] = (vote_tally[key] / vote_total) * 100

# Generate parallel lists to pull the winner of the election based on popular vote.
votes = list(vote_tally.values())
candidates = list(vote_tally.keys())

# Loop over dictionaries to produce f-strings for output
results_list = []
for name in candidate_list:
    results_list.append(f"{name}: {vote_pct[name]:.3f}% ({vote_tally[name]})")
vote_report = "\n".join(results_list)

# Generate f-string for output
output = f'''Election Results
-------------------------
Total Votes: {vote_total}
-------------------------
{vote_report}
-------------------------
Winner: {candidates[votes.index(max(votes))]}
-------------------------'''

# Print results in terminal
print(output)

# Write outputs to .txt
with open("Output.txt", 'w') as text_file:
    text_file.write(output)
