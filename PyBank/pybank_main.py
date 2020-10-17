import os
import csv

# Path to collect data from the PayPoll_Resources folder
filepath = os.path.join("PyBank", "PyBank_Resources", "budget_data.csv")

#
Months = []
ProfitsorLosses = []
Changes_PandL = []
# Read in the CSV file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        Months.append(row[0])
        ProfitsorLosses.append(int(row[1]))

    print(Months[1+1])

    for i in range(len(Months)):
        if ProfitsorLosses[i] == ProfitsorLosses [0]:
            ""
        else:    
            Datapoint = ProfitsorLosses [i] - ProfitsorLosses [i-1]
            Changes_PandL.append(Datapoint)

    TotalMonths = len(Months)
    Total = sum(ProfitsorLosses)
    AverageChange = sum(Changes_PandL) / len(Changes_PandL)    
    print(TotalMonths)
    print(Total)
    print(AverageChange)   
    