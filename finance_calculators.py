import math

# Prompt the user to select a calculator
while True:
    calculator_selection = input("""
      Which calculation would you like to do?
                             
      Investment - to calculate the amount of interest you'll earn on your investment.
                             
      Bond - to calculate the amount you'll have to pay on a home loan.
                             
      Enter either 'investment' or 'bond' from the menu above to proceed: """)
# INVESTMENT CALCULATOR
    if calculator_selection.lower() == "investment":
        P = int(input("How much would you like to invest? \n"))
        r = int(input("Interest rate? \n")) / 100
        t = int(input("How many years would you like to invest? \n"))
        interest_type = input("Do you want 'simple' or 'compound' interest? \n").lower()

        if interest_type == "simple":
            A = P * (1 + r * t)  # Simple interest calculation
        elif interest_type == "compound":
            A = P * math.pow((1 + r), t)  # Compound interest calculation
        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")
            continue

        print(f"The interest you will earn on your investment: R{A:.2f}")
        break
# BOND CALCULATOR
    elif calculator_selection.lower() == "bond":
        P = int(input("What is the present value of your house? "))
        i = float(input("Interest rate? ")) / 100 / 12
        n = int(input("Payment term in months? "))

        repayment = (i * P) / (1 - (1 + i) ** (-n))
        print(f"Your monthly repayment: R{repayment:.2f}")
        break

# If the user enters an invalid option, prompt them to try again
    else:
        print(f'You have entered an invalid input "{calculator_selection}". Try again.')