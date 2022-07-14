print("Welcome to the tip_calculator :)")

bill = float(input("Enter your total bill?: $"))

percentage_tip = int(
    input("What percentage tip would you like to give? 10, 12 or 20? ")
)

people = int(input("How many people to split the bill? "))

tip_as_percent = percentage_tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")
