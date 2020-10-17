import os
import csv

# Path to collect data from the PayPoll_Resources folder
filepath = os.path.join("PyBank", "PyBank_Resources", "budget_data.csv")
# Read in the CSV file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Loop through the data
    for row in csvreader:
        
        print(row)

        break