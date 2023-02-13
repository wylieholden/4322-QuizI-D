"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

CSVFILE = "employee_data.csv"

# open
infile = open(CSVFILE, "r", newline="")
reader = csv.reader(infile)
next(reader)

# create an empty dictionary
employee_salaries = {}

# use a loop to iterate through the csv file
for employee in reader:
    print(employee)
    


    # check if the employee fits the search criteria
for employee in reader:
    if (employee[3] == 'Marketing' or 'Management'
        
        employee[1] = {employee[5]}




print(eq_dict)
print()


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
