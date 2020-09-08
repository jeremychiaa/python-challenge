# PyBank
# Import modules
import os
import csv

# Path to collect data from resources folder
budget_csv = os.path.join(r'C:\Users\jerem\Desktop\REPOS\python-challenge\Resources\budget_data.csv')

# Lists to store data
total_months = []
profit_loss = []
monthly_change = []
average_change = []
greatest_increase = []
greatest_decrease = []

# Read in the CSV file
with open(budget_csv, newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Skip header in CSV file
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Add row data sets into lists
        total_months.append(row[0])
        profit_loss.append(row[1])

    # Total number of months included in the dataset
    print(len(total_months))

    # Net total amount of profit/losses over entire period
    net_profit_loss = sum(map(int, profit_loss))
    print(net_profit_loss)

    # Set initial value of i = 0
    i = 0

    #Loop through all rows in profit/losses column
    for i in range(len(profit_loss) - 1):
        monthly_diff = int(profit_loss[i+1]) - int(profit_loss[i])
        
        # Append monthly_diff into list
        monthly_change.append(monthly_diff)

    # Average of the changes in profit/losses over entire period
    average_change = sum(monthly_change) / len(monthly_change)
    print(average_change)


        # Greatest increase in profits over entire period

        #print(total_months)
        #print(net_profit_loss)
        


