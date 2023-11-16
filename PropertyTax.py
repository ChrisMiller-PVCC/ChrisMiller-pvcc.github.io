# Name: Christopher Miller
# Program Purpose: This program calculates semi-annual personal property tax owed for a vehicle.


import datetime

# Define global constants
TAX_RATE = 0.042
RELIEF_RATE = 0.33
DUE_DATE = 'Dec. 09, 2023'

# Define global variables
relief_eligible = 0
assessment = 0
tax_amount = 0
relief_amount = 0
amount_due = 0


def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yes_no = input(
            "\nWould you like to calculate personal property tax for another vehicle? (Y or N): ")
        if yes_no.upper() == "N":
            more = False
            print(f'Please be sure to pay in full by {DUE_DATE}.')


def get_user_data():
    global relief_eligible, assessment
    relief_eligible = input(
        "Is your vehicle eligible for tax relief? (Y or N): ").upper()
    assessment = int(input("What is the value of your vehicle?: "))


def perform_calculations():
    global tax_amount, relief_amount, amount_due
    if relief_eligible == 'Y' or relief_eligible == 'YES':
        relief_amount = assessment * TAX_RATE * RELIEF_RATE / 2
    else:
        relief_amount = 0
    tax_amount = assessment * TAX_RATE / 2
    amount_due = tax_amount - relief_amount


def display_results():
    money_format = '12,.2f'
    print('-----------------------------------------')
    print('*** Charlottesville, Virginia. ***')
    print('-----------------------------------------')
    print('Months taxed: 6')
    print(f'Due date: {DUE_DATE}')
    print('-----------------------------------------')
    print(f'Assessed value             $ {assessment:{money_format}}')
    print(f'Full tax amount            $ {tax_amount:{money_format}}')
    print(f'Relief                     $ {relief_amount:{money_format}}')
    print(f'\nTotal amount due           $ {amount_due:{money_format}}')
    print('-----------------------------------------')
    print(f'Total due {DUE_DATE}: ${amount_due:{money_format}}')
    print(datetime.datetime.now())


if __name__ == "__main__":
    main()
