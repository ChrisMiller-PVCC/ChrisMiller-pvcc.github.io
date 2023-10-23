# Name: Christopher Miller, Felix Barrientos, Gabe
# Prog Purpose: Branch Barbecue Buffet
# Price for Adults: $19.95
# Price for children $11.95
# Sales tax rate: 6.2%
# Service fee rate: 10%
import datetime

############ define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .062
PR_ADULT = 19.95
PR_CHILD = 11.95
SERVICE_FEE = 0.1

# define global variables
num_adult = 0
num_children = 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0
adult = 0
child = 0
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
            print('Thank you for your order. Enjoy your food!')
    
def get_user_data():
    global num_adult
    global num_children
    num_adult = int(input("Number of Adults: "))
    num_children = int(input("Number of Children: "))

def perform_calculations():
    global subtotal, sales_tax, total, service_fee, adult, child
    
    adult = num_adult * PR_ADULT
    child = num_children * PR_CHILD
    subtotal = adult + child
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee
    

def display_results():
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** Branch BBQ Buffet ****')
    print('World Famous Barbecue House')
    print(line)
    print('Adults       $ ' + format(adult, '8,.2f'))
    print('Children     $ ' + format(child, '8,.2f'))
    print('Subtotal     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax, '8,.2f'))
    print('Service Fee  $ ' + format(service_fee, '8,.2f'))
    print('Total        $ ' + format(total, '8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))


############ call on main program to execute ############
main()
