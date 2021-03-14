import os
import csv

# Path to collect data from the PayPoll_Resources folder
filepath = os.path.join("PyBank", "PyBank_Resources", "budget_data.csv")

#Lists created / tickers used:
Months = [] #List comprising all months (i.e. values under 'Date' column)
ProfitsorLosses = [] #List comprising all values under 'Profit/Losses' column
Changes_PandL = [] #List comprising the changes in profit/losses from one month to the other (i.e. Changes_Profits and Losses)

# Read in the CSV file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
#We need to erase the header row:
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        Months.append(row[0])
        #We add all items under the 'Date' column to the 'Months' list. We now have a list with all the dates of our database.
        ProfitsorLosses.append(int(row[1]))
        #We add all items under the 'Profit/Losses' column to the 'ProfitsorLosses' list. We now have a list with all the profits/losses of our database.
    
    #We need to generate a list of the changes in Profit/Losses over time. We compare the Profits/Losses in a month vs. the Profits/Losses in the PRIOR month: 
    for i in range(len(Months)):
        if ProfitsorLosses[i] == ProfitsorLosses [0]: #Of course, there is no Profits/Losses datapoints before the first entry. We account for this through an if statement.
            ""
        else: #We find the difference in Profits/Losses of month 'x'(e.g. February) and month 'x-1' (e.g. January). Each of these substractions is added to the 'Changes_PandL' list   
            Datapoint = ProfitsorLosses [i] - ProfitsorLosses [i-1]
            Changes_PandL.append(Datapoint)
    
    #We loop through our list of changes in Profit/Losses over time.
    for w in range(len(Changes_PandL)):
        if Changes_PandL[w] == min(Changes_PandL):
            GreatestDecDate = Months[w+1]   #We find the month associated to the greatest decrease in losses
        elif Changes_PandL[w] == max(Changes_PandL):
            GreatestIncDate = Months[w+1] #We find the month associated to the greatest increase in profits

    #RESPONSES TO THIS EXERCISE
    #Total months in dataset
    TotalMonths = f"Total Months: {len(Months)}" #Total months in dataset = Number of items in the 'Months' list. We write a string with the exact wording & format requested in the instructions
    #net total amount of Profits/Losses
    Total = f"Total: ${sum(ProfitsorLosses)}" # Net amount of Profits/Losses = Adding all items in the 'ProfitsorLosses' list. We write a string with the exact wording & format requested in the instructions
    #Average of changes in Profits/Losses
    AverageChange = f"Average Change: ${round(sum(Changes_PandL) / len(Changes_PandL),2)}" #We sum the values of all the items in the 'Changes_PandL' list and divide this figure by the number of items to find the average. We write a string with the exact wording & format requested in the instructions
    #Greatest increase in Profits
    GreatestInc = f"Greatest Increase in Profits: {GreatestIncDate} (${max(Changes_PandL)})" #We write a string including the date and greatest increase in Profits as requested in the instructions.
    #Greatest decrease in Losses
    GreatestDec = f"Greatest Decrease in Profits: {GreatestDecDate} (${min(Changes_PandL)})" #We write a string including the date and greatest decrease in Losses as requested in the instructions.   
    #Final Answer
    PyBankAnswer = "Financial Analysis" + "\n" + "----------------------------" + "\n" + TotalMonths + "\n" + Total + "\n" + AverageChange + "\n" + GreatestInc + "\n" + GreatestDec
    #We add all the strings to generate the exact text requested as the answer.
    print(PyBankAnswer)

#We create a text file, and save it under the PyBank folder:
filename = "PyBank/PyBankAnwer.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename,"w") as datafile:
    writer = csv.writer(datafile)
    datafile.write(PyBankAnswer)