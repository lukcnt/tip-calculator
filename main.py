#Greeting.
print("Welcome to the tip calculator.")

#Total bill amount input from the user.
total_bill = input("What was the total bill: $")

#Percentage of the tip.
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_percentage = percentage / 100

#Number of people who will split the bill.
number_people = int(input("How many people to split the bill? "))