#change directory to python-challenge
#change directory to Pybank

# import library
import os
import csv

#determine csv path
Pybankcsv = 'Resources/budget_data.csv'

# open and read csv file through the scv path & read the header row first (skip this step if there is no header)
with open(Pybankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # create list to store data of amount of profit and loss & month
    Profit = []
    Month = []
    monthly_changes =[]

    # loops through each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        Month.append(rows[0])

    for x in range(1, len(Profit)):
        monthly_changes.append((int(Profit[x]) - int(Profit[x-1])))

    # calculate average monthly change
    monthly_change_average = sum(monthly_changes) / len(monthly_changes)
    monthly_average = round(monthly_change_average, 2)

    # calculate total length of month
    Total_month = len(Month)

    # find greatest increase & decrease in revenue
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    # print results
    print ("Financial Analysis")

    print("....................................................................................")

    print ("Total Month:" + str(Total_month))

    print("Total:" + "$" + str(sum(Profit)))

    print ("Average Change:" + "$" + str(monthly_average))

    print("Greatest Increase in Profits: " + str(Month[monthly_changes.index(max(monthly_changes))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(Month[monthly_changes.index(min(monthly_changes))+1]) + " " + "($" + str(greatest_decrease) + ")")

    #spesify location of the path to write
    folder_path = 'Analysis'
    os.makedirs(folder_path)

    #create a new file in the spesified folder
    file_name = "output.txt"
    file_path = os.path.join(folder_path, file_name)    
    file = open(file_path, "w")

    # output to a text file
    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("Total months: " + str(Total_month) + "\n")

    file.write("Total: " + "$" + str(sum(Profit)) + "\n")

    file.write("Average change: " + "$" + str(monthly_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(Month[monthly_changes.index(max(monthly_changes))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(Month[monthly_changes.index(min(monthly_changes))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()
