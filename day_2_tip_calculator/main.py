print("Welcome to the tip calculator! Follow the prompts to calculate your tip.")
initial_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10 12 15 "))
num_people = int(input("How many people to split the bill? "))
tip_as_percent = tip_percentage / 100
total_tip_amount = initial_bill * tip_as_percent
total_bill = initial_bill + total_tip_amount
bill_per_person = total_bill / num_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")