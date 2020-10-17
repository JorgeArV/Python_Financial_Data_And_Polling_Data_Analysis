import os
import csv

# Path to collect data from the PayPoll_Resources folder
filepath = os.path.join("PyPoll", "PyPoll_Resources", "election_data.csv")

#Lists created / tickers used:
Votes= [] #List comprising all votes
ListofC =[] # List comprising all candidates
KhanCounter = 0 #Counter of votes given to Khan
CorreyCounter = 0 #Counter of votes given to Correy
LiCounter = 0 #Counter of votes given to Li
OTooleyCounter = 0 #Counter of votes given to O'Tooley


# Read in the CSV file:
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
#We need to erase the header row:
    header = next(csvreader)

    # We add all items under the 'Candidate' column to the 'Votes' list. We now have a list with all the votes in town.
    for row in csvreader:
        Votes.append(row[2])
    #We search the 'Votes' list for all unique values (i.e. candidates), and add these unique values to the ListofC (i.e. list of candidates) list. We now have a list with all the candidates.
    for i in Votes:
        if i not in ListofC:
            ListofC.append(i)
    print(f"These are the candidates {ListofC}") #after printing the ListofC list, we know there are four candidates: Khan, Correy, Li and O'Tooley

    #We loop through the 'Votes' list:
    for z in range(len(Votes)):
        #Khan's index in 'ListofC' is 0. We add a vote to Khan's Counter for every time a vote = "Khan"
        if Votes[z] == ListofC[0]:
            KhanCounter = KhanCounter + 1
        #Correy's index in 'ListofC' is 1. We add a vote to Correy's Counter for every time a vote = "Correy"
        elif Votes[z] == ListofC[1]:
            CorreyCounter = CorreyCounter + 1
        #Li's index in 'ListofC' is 2. We add a vote to Li's Counter for every time a vote = "Li"
        elif Votes[z] == ListofC[2]:
            LiCounter = LiCounter + 1
        #O'Tooley's index in 'ListofC' is 3. We add a vote to O'Tooley's Counter for every time a vote = "O'Tooley"
        elif Votes[z] == ListofC[3]:
            OTooleyCounter = OTooleyCounter + 1    

    #We create a list with all the counters.
    VotesperC = [KhanCounter, CorreyCounter, LiCounter, OTooleyCounter]
    if max(VotesperC) == KhanCounter: #if the item with the max value of the list = KhanCounter, then Khan is the winner
        Winner = "Khan"
    elif max(VotesperC) == CorreyCounter: #if the item with the max value of the list = CorreyCounter, then Correy is the winner
        Winner = "Correy"
    elif max(VotesperC) == LiCounter: #if the item with the max value of the list = LiCounter, then Li is the winner
        Winner = "Li"
    else: #If none of the other 3 candidates has the max. number of votes, then O'Tooley must be the winner
        Winner = "O'Tooley" 

#RESPONSES TO THIS EXERCISE
#Total votes
    TotalVotes = len(Votes) #Total votes = number of items in the 'Votes' list.
    TotalVotesStatement = f"Total Votes: {TotalVotes}" #We write a string with the exact wording & format requested in the instructions
#KhanResults
    KhanResults = f"Khan: {round(KhanCounter/TotalVotes*100,3)}00% ({KhanCounter})"
    #We divide KhanCounter by the total votes to get their % of votes. We write a string with the exact wording & format requested in the instructions.
#CorreyResults
    CorreyResults = f"Correy: {round(CorreyCounter/TotalVotes*100,3)}00% ({CorreyCounter})"
    #We divide CorreyCounter by the total votes to get their % of votes. We write a string with the exact wording & format requested in the instructions.
#LiResults
    LiResults = f"Li: {round(LiCounter/TotalVotes*100,3)}00% ({LiCounter})"
    #We divide LiCounter by the total votes to get their % of votes. We write a string with the exact wording & format requested in the instructions.
#O'TooleyResults
    OTooleyResults = f"O'Tooley: {round(OTooleyCounter/TotalVotes*100,3)}00% ({OTooleyCounter})"
    #We divide OTooleyCounter by the total votes to get their % of votes. We write a string with the exact wording & format requested in the instructions.
#Winner
    WinnerStatement = f"Winner: {Winner}"
    #We write the 'winner' statement with the exact wording & format requested in the instructions"
#Final Answer
    PyPollAnswer = "Election Results" + "\n" + "-------------------------" + "\n" + TotalVotesStatement + "\n" + "-------------------------" + "\n" + KhanResults + "\n" + CorreyResults + "\n" + LiResults + "\n" + OTooleyResults + "\n" +"-------------------------" + "\n" + WinnerStatement + "\n" + "-------------------------"
    #We add all the strings to generate the exact text requested as the answer
    print(PyPollAnswer)

#We create a text file, and save it under the PyPoll folder:
filename = "PyPoll/PyPollAnwer.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename,"w") as datafile:
    writer = csv.writer(datafile)
    datafile.write(PyPollAnswer)

