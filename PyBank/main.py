#change directory to python-challenge
#change directory to Pybank

# import library
import os
import csv

#join path
csvpath = 'Resources/budget_data.csv'

# open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # find net amount of profit and loss
    P = []
    months = []

    # read each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change =[]

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))

    # calculate average revenue change
    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)

    #greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print Results
    print ("Financial Analysis")

    print("....................................................................................")

    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(P)))

    print ("Average Change:" + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")

    #spesify location of the path to write
    folder_path = 'Analysis'
    os.makedirs(folder_path)

    #create a new file in the above folder
    file_name = "output.txt"
    file_path = os.path.join(folder_path, file_name)    
    file = open(file_path, "w")

    # output to a text file

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()