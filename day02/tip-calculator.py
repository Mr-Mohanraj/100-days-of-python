print("####### Welcome to the tip_calculator #######")

bill = float(input("Enter your total bill?: $"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 20? "))

people = int(input("How many people to split the bill? "))

"""percentage formula = (values / 100) * 100."""
tip_as_percent = (percentage_tip / 100) * 100 

total_bill = bill + tip_as_percent

bill_per_person = total_bill / people
 
# round function roundup the result after the dot(.),second permeter for how many number after the dot(.)/
# EX: input = 22.3343 return values of the function : 22.33

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")


def bugFreeVersion():
    print("####### Welcome to the tip_calculator #######")

    bill = float(input("Enter your total bill?: $"))

    percentage_tip = float(
        input("What percentage tip would you like to give? 10, 12 or 20? ")
    )

    people = int(input("How many people to split the bill? "))
    
    if bill > 0 and percentage_tip > 0 and people > 0:

        """percentage formula = (values / 100) * 100."""

        tip_as_percent = (percentage_tip / 100) * 100 

        total_bill = bill + tip_as_percent

        bill_per_person = total_bill / people
         
        # round function roundup the result after the dot(.),second permeter for how many number after the dot(.)/
        # EX: input = 22.3343 return values of the function : 22.33
        final_amount = round(bill_per_person, 2)

        final_amount = "{:.2f}".format(bill_per_person)

        print(f"Each person should pay ${final_amount}")
    else:
        print("You Enter negative values")
    