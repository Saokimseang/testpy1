while True:
    # Get input
    weight = float(input("Input your weight (in kg): "))  # 80
    height = float(input("Input your height (in meters): "))  # 1.73

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Output the result
    print(f"Your BMI: {int(bmi)}")

    # input again
    again = input("Do you want to calculate BMI again? (yes/no): ").strip().lower()
    if again != 'yes':
        break
