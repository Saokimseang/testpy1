while True:
    print("==== Welcome to Tip Calculator ====")

    # input from the user
    total_bill = float(input("What was the total bill? : $"))
    tip_percentage = int(input("How much tip would you like to give? 10, 12, 15? : "))
    num_people = int(input("How many people to split the bill? : "))

    #
    tip_amount = total_bill * (tip_percentage / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / num_people

    # Output the result
    print(f"Each person should pay: ${amount_per_person:.2f}")

    # calculate again
    again = input("Do you want to calculate another tip? (yes/no): ").strip().lower()
    if again != 'yes':
        break
