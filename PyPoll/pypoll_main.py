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

    #Create
    VotesperC = [KhanCounter, CorreyCounter, LiCounter, OTooleyCounter]
    if max(VotesperC) == KhanCounter:
        Winner = "Khan"
    elif max(VotesperC) == CorreyCounter:
        Winner = "Correy"
    elif max(VotesperC) == LiCounter:
        Winner = "Li"
    else:
        Winner = "O'Tooley"

#Total votes
    TotalVotes = len(VoterID)
    TotalVotesStatement = f"Total Votes: {TotalVotes}"
#KhanResults
    KhanResults = f"Khan: {round(KhanCounter/TotalVotes*100,3)}00% ({KhanCounter})"
#CorreyResults
    CorreyResults = f"Correy: {round(CorreyCounter/TotalVotes*100,3)}00% ({CorreyCounter})"
#LiResults
    LiResults = f"Li: {round(LiCounter/TotalVotes*100,3)}00% ({LiCounter})"
#O'TooleyResults
    OTooleyResults = f"O'Tooley: {round(OTooleyCounter/TotalVotes*100,3)}00% ({OTooleyCounter})"
    #Winner
    WinnerStatement = f"Winner: {Winner}"

    PyPollAnswer = "Election Results" + "\n" + "-------------------------" + "\n" + TotalVotesStatement + "\n" + "-------------------------" + "\n" + KhanResults + "\n" + CorreyResults + "\n" + LiResults + "\n" + OTooleyResults + "\n" +"-------------------------" + "\n" + WinnerStatement + "\n" + "-------------------------"

    print(PyPollAnswer)

#Creating a text file:
filename = "PyPoll/PyPollAnwer.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename,"w") as datafile:
    writer = csv.writer(datafile)
    datafile.write(PyPollAnswer)

