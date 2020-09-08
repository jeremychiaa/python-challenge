# PyBank
# Import modules
import os
import csv

# Path to collect data from resources folder
budget_csv = os.path.join(r'C:\Users\jerem\Desktop\REPOS\python-challenge\Resources\budget_data.csv')

# Create empty lists to store data
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

        # Add row data into lists
        total_months.append(row[0])
        profit_loss.append(row[1])

    # Net total amount of profit/losses over entire period
    net_profit_loss = sum(map(int, profit_loss))

    #Loop through all rows in profit/losses column
    # Set initial value of i = 0
    i = 0
    for i in range(len(profit_loss) - 1):
        monthly_diff = int(profit_loss[i+1]) - int(profit_loss[i])
        
        # Add monthly_diff into list
        monthly_change.append(monthly_diff)

    # Average of the changes in profit/losses over entire period
    average_change = sum(monthly_change) / len(monthly_change)

    # Greatest increase in profits over entire period
    greatest_increase = max(monthly_change)
    
    # Retrieve index of month with greatest increase
    j = monthly_change.index(greatest_increase)
    greatest_increase_month = total_months[j+1]

    # Greatest decrease in losses over entire period
    greatest_decrease = min(monthly_change)

    # Retrieve index of month with greatest decrease
    k = monthly_change.index(greatest_decrease)
    greatest_decrease_month = total_months[k+1]

    # Print results
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(total_months)}')
    print(f'Total: {net_profit_loss}')
    print(f'Average Change ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')