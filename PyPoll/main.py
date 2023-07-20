'read in csv'
import os
import csv 


#read csv and create analysis txt file
pypoll_report = open('analysis/Report.txt','w')
poll_data = csv.reader(open('Resources/election_data.csv'))

#store header 
pypoll_header = next(poll_data)


#create variables 
total_votes = 0 
candidate_vote_1 = 0 
candidate_vote_2 = 0
candidate_vote_3 = 0

#separate candidate vote variables - Saad 
#create loop to go through our rows 
for row in poll_data:
    
    #CALCULATE THE TOTAL NUMBER OF VOTES
    total_votes = total_votes +1
    
    candidate = row[2]
    
    #Loop through candidate names with if statement
    if candidate == "Charles Casper Stockham":
       candidate_vote_1 = candidate_vote_1 + 1
            
    elif candidate == "Diana DeGette":
        candidate_vote_2 = candidate_vote_2 +1

    elif candidate == "Raymon Anthony Doane":
        candidate_vote_3 = candidate_vote_3 +1
    
    #calculate the percentage for each candidate
    candidate_1_percent = (candidate_vote_1/total_votes)*100
    candidate_2_percent = (candidate_vote_2/total_votes)*100
    candidate_3_percent = (candidate_vote_3/total_votes)*100



#print the output table by filling in with variables
poll_output = f'''

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {candidate_1_percent:,.3f}% ({candidate_vote_1})
Diana DeGette: {candidate_2_percent:,.3f}% ({candidate_vote_2})
Raymon Anthony Doane: {candidate_3_percent:,.3f}% ({candidate_vote_3})
-------------------------
Winner: Diana DeGette
'''

#print results 
print(poll_output)
pypoll_report.write(poll_output)