# Name: Christopher Miller
# Prog Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Sales tax rate: 5.5%
# Price for a bucket of popcorn: $8.99
import datetime

############ define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 8.99

# define global variables
num_popcorn = 0
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############ define program functions ############


def main():
    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "N":
            more_tickets = False
            print('Thank you for your order. Enjoy your movie!')
    
def get_user_data():
    global num_tickets
    global num_popcorn
    num_tickets = int(input("Number of movie tickets: "))
    num_popcorn = int(input("Number of buckets of popcorn: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET + num_popcorn * PR_POPCORN
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyformat = '8,.2f'
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('------------------------------')
    print('Tickets       $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax     $ ' + format(sales_tax, '8,.2f'))
    print('Total         $ ' + format(total, '8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))


############ call on main program to execute ############
main()
