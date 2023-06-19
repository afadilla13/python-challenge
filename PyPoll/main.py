#change directory to python-challenge
#change directory to Pypoll

# import Pypoll
import os
import csv

# open and read csv
PyPoolcsv = os.path.join('Resources','election_data.csv')
with open(PyPoolcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Declares variables
    CCS_votes = 0
    DD_votes = 0
    RAD_votes = 0
    
    # Create list to store data
    votes = []
    county = []
    candidates = []
    CCS = []
    DD = []
    RAD = []

    # read each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Total vote count
    Total_votes = (len(votes))

    # Votes by each candidates
    for x in candidates:
        if x == "Charles Casper Stockham":
            CCS.append(candidates)
            CCS_votes = len(CCS)
            
        elif x == "Diana DeGette":
            DD.append(candidates)
            DD_votes = len(DD)
            
        else:
            RAD.append(candidates)
            RAD_votes = len(RAD)
    
    # Find percentages for each candidates
    CCS_percent = round(((CCS_votes / Total_votes) * 100), 3)
    DD_percent = round(((DD_votes / Total_votes) * 100), 3)
    RAD_percent = round(((RAD_votes / Total_votes) * 100), 3)

    # If statement for the winner 
    if CCS_percent > max(DD_percent, RAD_percent):
        winner = "Charles_Casper_Stockham"
    elif DD_percent > max(CCS_percent, RAD_percent):
        winner = "Diana_DeGette"  
    else:
        winner = "Raymon_Anthony_Doane"

    #spesify location of the path to write
    folder_path = 'Analysis'
    os.makedirs(folder_path)

    #create a new file in the above folder
    file_name = "output.txt"
    file_path = os.path.join(folder_path, file_name)    
    file = open(file_path, "w")

    # Print Statements
    print(f'''Election Results
-----------------------------------
Total Votes: {Total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {CCS_percent}% ({CCS_votes})
Diana_DeGette: {DD_percent}% ({DD_votes})
Raymon_Anthony_Doane: {RAD_percent}% ({RAD_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

    # Output to a text file
    file.write(f'''Election Results
-----------------------------------
Total Votes: {Total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {CCS_percent}% ({CCS_votes})
Diana_DeGette: {DD_percent}% ({DD_votes})
Raymon_Anthony_Doane: {RAD_percent}% ({RAD_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

    file.close()
