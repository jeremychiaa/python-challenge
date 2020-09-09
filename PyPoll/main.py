#PyPoll
#Import modules
import os
import csv

# Path to collect data from resources folder
election_csv = os.path.join(r'C:\Users\jerem\Desktop\REPOS\python-challenge\Resources\election_data.csv')

# Create empty lists to store data
voter_id = []

# Read in the CSV file
with open(election_csv, newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header in CSV file
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        voter_id.append(row[0])
    
    # Print total number of votes
    print(len(voter_id))