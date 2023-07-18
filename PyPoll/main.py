'read in csv'
import os
import csv 

poll_data = csv.reader(open('Resources/election_data.csv'))

next(poll_data)

#create variables 
total_votes = 0 
candidate_vote = 0 

#create loop to go through our rows 
for row in poll_data:
    
    #CALCULATE THE TOTAL NUMBER OF VOTES
    total_votes = total_votes +1
    
    candidate = [2]
    
    #Loop through candidate names 
    if candidate == ["Charles Casper Stockham"]:
       candidate_vote = candidate_vote + 1

    elif candidate == ["Diana DeGette"]:
        candidate_vote = candidate_vote +1

    elif candidate == ["Raymon Anthony Doane"]:
        candidate_vote = candidate_vote +1



#print the output table
poll_output = f'''

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: 23.049% ({candidate_vote})
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
'''

print(poll_output)
