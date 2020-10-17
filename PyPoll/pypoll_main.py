import os
import csv

# Path to collect data from the PayPoll_Resources folder
filepath = os.path.join("PyPoll", "PyPoll_Resources", "election_data.csv")

#
VoterID = []
Votes= []
ListofC =[]
KhanCounter = 0
CorreyCounter = 0
LiCounter = 0
OTooleyCounter = 0

# Read in the CSV file
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        VoterID.append(row[0])
        Votes.append(row[2])
    
    for i in Votes:
        if i not in ListofC:
            ListofC.append(i)
    print(ListofC) 

    for z in range(len(Votes)):
        if Votes[z] == ListofC[0]:
            KhanCounter = KhanCounter + 1
        elif Votes[z] == ListofC[1]:
            CorreyCounter = CorreyCounter + 1
        elif Votes[z] == ListofC[2]:
            LiCounter = LiCounter + 1
        elif Votes[z] == ListofC[3]:
            OTooleyCounter = OTooleyCounter + 1    
    print(KhanCounter) 
    print(CorreyCounter)
    print(LiCounter)
    print(OTooleyCounter)

        
#Total votes
    TotalVotes = len(VoterID)
    print(TotalVotes)   
