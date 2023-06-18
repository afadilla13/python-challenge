#change directory to python-challenge
#change directory to Pypoll

# import Pypoll
import os
import csv

# open and read csv
csvpath=os.path.join('Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # Declaring variables
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # read each row of data after header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # VOTE COUNT
    total_votes = (len(votes))
    # print(total_votes)

    # Votes by Person
    for x in candidates:
        if x == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)
            Charles_Casper_Stockham_votes = len(Charles_Casper_Stockham)
            
        elif x == "Diana DeGette":
            Diana_DeGette.append(candidates)
            Diana_DeGette_votes = len(Diana_DeGette)
            
        else:
            Raymon_Anthony_Doane.append(candidates)
            Raymon_Anthony_Doane_votes = len(Raymon_Anthony_Doane)
    
    # print(Charles_Casper_Stockham_votes)
    # print(Diana_DeGette_votes)
    # print(Raymon_Anthony_Doane_votes)
    
    
    # Percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
    # print(Charles_Casper_Stockham_percent)
    # print(Diana_DeGette_percent)
    # print(Raymon_Anthony_Doane_percent)

    
    # Winner 
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
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
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')


    # Output to a text file
    file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

    file.close()