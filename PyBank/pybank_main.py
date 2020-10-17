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

    for i in range(len(Months)):
        if ProfitsorLosses[i] == ProfitsorLosses [0]:
            ""
        else:    
            Datapoint = ProfitsorLosses [i] - ProfitsorLosses [i-1]
            Changes_PandL.append(Datapoint)
    
    for w in range(len(Changes_PandL)):
        if Changes_PandL[w] == min(Changes_PandL):
            GreatestDecDate = Months[w+1]
        elif Changes_PandL[w] == max(Changes_PandL):
            GreatestIncDate = Months[w+1]

    TotalMonths = len(Months)
    Total = sum(ProfitsorLosses)
    AverageChange = sum(Changes_PandL) / len(Changes_PandL)
    GreatestInc = max(Changes_PandL)
    GreatestDec = min(Changes_PandL)    
    #print(TotalMonths)
    #print(Total)
    #print(AverageChange)
    #print(GreatestInc)
    #print(GreatestDec) 
    #print(GreatestIncDate) 
    #print(GreatestDecDate)

    #Intro = print("Financial Analysis")
    #Line = print ("--------------------------------------------------------------------")
    Statement = f"Financial Analysis: {/n} Total Months: {TotalMonths}   Total:${Total}   Average Change: ${round(AverageChange,2)} Greatest Increase in Profits: {GreatestIncDate} (${GreatestInc})   Greatest Decrease in Profits: {GreatestDecDate} (${GreatestDec})  "
    print(Statement)
    #Final_Answer: f"{TotalMonths}
    #print(Final_Answer)
#Creating a text file:
#filename = "PyBank/PyBankAnwer.txt"
#os.makedirs(os.path.dirname(filename), exist_ok=True)

#with open(filename,"w") as datafile:
#    writer = csv.writer(datafile)
#    datafile.write(Statement)