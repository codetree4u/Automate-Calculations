# coding: utf-8
import csv
from pathlib import Path

print("Part 1: Automate the Calculations")
"""Part 1: Automate the Calculations.
"""
loan_costs = [500, 600, 200, 1000, 450]

# len function counts the number of loans.
number_of_loans = len(loan_costs)
# Print variable
print(f"The total number of loans is " , number_of_loans)

# sum function adds all values from the list.
sum_loans = sum(loan_costs)
# Print variable
print(f"The total value of all loans is $" , sum_loans)

# Set average loan value from prior variables.
average_loans = sum_loans / number_of_loans
# Print variable.
print(f"The average loan value is  $", average_loans)


print("Part 2: Analyze Loan Data.")
"""Part 2: Analyze Loan Data.
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Future value extracted from a list.
future_value = loan.get("future_value")
# Printing variable.
print(f"The loan future value is $", future_value)

# Remaining months value extracted from a list.
remaining_months = loan.get("remaining_months")
# Printing variable.
print(f"The loan remaining months are ", remaining_months,"Months")

# Formula calculates Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
present_value = (future_value) / (1 + .20/12) ** (remaining_months)

# If the present value of the loan is greater than or equal to the cost, then print message.
if present_value >= 500:
    print(f"The loan is worth buying because PV ${present_value:.2f} is greater or equal than loan price of $ 500")
# Else, the present value of the loan is less than the loan cost    
else:
    print("The loan is too expensive and not worth the price because PV ${present_value:.2f} is less or equal than $ 500.")

print("Part 3: Perform Financial Calculations.")
"""Part 3: Perform Financial Calculations.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Function accepts 2 params from a list and 1 percentage value as the third param. 
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + (annual_discount_rate)/12) ** remaining_months
    return present_value

# Calling function and storing its return into a variable.
p_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate=0.20)

# Displaying present value.
print(f"The present value of the loan is ${p_value:.2f}")

print("Part 4: Conditionally filter lists of loans.")
"""Part 4: Conditionally filter lists of loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


# set an empty list.
inexpensive_loans = []

# Create a for loop to append any loan less than $500 and append to a list.
for item in loans:
    if item["loan_price"] > 500:
        inexpensive_loans.append(item)

# printing a list content 1 row at a time.
print(f"This is the inexpensive loans list:",'\n1- {0}\n2- {1}'.format(*inexpensive_loans))

print("Part 5: Save the results.")
print("Writing the data to a CSV file...")
"""Part 5: Save the results. 
"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Open the output CSV file path using `with open`
with open (output_path, 'w' , newline='') as csvfile:
    # Set a writing object.
    csvwriter = csv.writer(csvfile, delimiter = ',')
    # csvwrite is writting the csv file header.
    csvwriter.writerow(header)
    # item is a row in the csv file.
    for item in inexpensive_loans:
        # csvwrite is writting the rows to the csv file.
        csvwriter.writerow(item.values())
