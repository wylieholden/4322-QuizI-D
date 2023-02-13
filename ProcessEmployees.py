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
# for employee in reader:
# print(employee)
print()
# check if the employee fits the search criteria
for employee in reader:
    if employee[3] == "Management" or "Marketing":
        print(employee[3], employee[5])

for employee in reader 
    if employee[3] == "Management" or "Marketing":
        print(employee[3], (employee[5] *1.1))


print()
print()


print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
