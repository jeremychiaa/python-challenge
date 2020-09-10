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
    print(total_votes)

    # Complete list of candidates who received votes
    # Se initial value of i to 0
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

    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)

    # Percentage of votes each candidate won
    khan_votes_percentage = round(((len(khan) / total_votes) * 100), 3)
    correy_votes_percentage = round(((len(correy) / total_votes) * 100), 3)
    li_votes_percentage = round(((len(li) / total_votes) * 100), 3)
    otooley_votes_percentage = round(((len(otooley) / total_votes) * 100), 3)

    print(khan_votes_percentage)
    print(correy_votes_percentage)
    print(li_votes_percentage)
    print(otooley_votes_percentage)

