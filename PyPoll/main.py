#PyPoll
#Import modules
import os
import csv

# Path to collect data from resources folder
election_csv = os.path.join(r'C:\Users\jerem\Desktop\REPOS\python-challenge\Resources\election_data.csv')

# Create empty lists to store data
voter_id = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

# Read in the CSV file
with open(election_csv, newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header in CSV file
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    # Print total number of votes
    total_votes = len(voter_id)

    # Run conditionals to determine each candidate's vote number
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)

        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)

        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

    # Percentage of votes each candidate won
    khan_votes_percentage = round(((len(khan) / total_votes) * 100), 3)
    correy_votes_percentage = round(((len(correy) / total_votes) * 100), 3)
    li_votes_percentage = round(((len(li) / total_votes) * 100), 3)
    otooley_votes_percentage = round(((len(otooley) / total_votes) * 100), 3)

    # Conditionals to determine winner of the election based on popular vote
    if khan_votes_percentage > max(correy_votes_percentage, li_votes_percentage, otooley_votes_percentage):
        winner = "Khan"
    elif correy_votes_percentage > max(khan_votes_percentage, li_votes_percentage, otooley_votes_percentage):
        winner = "Correy"
    elif li_votes_percentage > max(khan_votes_percentage, correy_votes_percentage, otooley_votes_percentage):
        winner = "Li"
    else:
        winner = "O'Tooley"
    
    # Print Results
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    print(f'Khan: {khan_votes_percentage}% ({khan_votes})')
    print(f'Correy: {correy_votes_percentage}% ({correy_votes})')
    print(f'Li: {li_votes_percentage}% ({li_votes})')
    print(f"O'Tooley: {otooley_votes_percentage}% ({otooley_votes})")
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")