# Name: Christopher Miller, damarion bright 
# # Prog Purpose: This program finds the order total for a pizza order
# Sales tax rate: 5.5%





import datetime

# Define tax rate and prices
SALES_TAX_RATE = 0.055
PR_DRINK = 3.99
PR_BREADSTICKS = 6.99
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 17.99
PR_XLARGE = 21.99

# Define global variables
num_pizza = 0
num_breadsticks = 0
num_drinks = 0
pizza_price = 0
pizza_cost = 0
subtotal = 0
sales_tax = 0
total = 0

def main():
    more_pizza = True

    while more_pizza:
        get_user_data()
        perform_calculations()
        display_results()

        ask_again = input("\nWould you like to order again (Y or N)?: ")
        if ask_again.upper() == "N":
            more_pizza = False
            print('Thank you for your order. Enjoy your food!')

def get_user_data():
    global num_pizza, num_breadsticks, num_drinks
    num_pizza = int(input("How many pizzas would you like?: "))
    num_breadsticks = int(input("How many breadsticks would you like?: "))
    num_drinks = int(input("How many drinks would you like? "))

def perform_calculations():
    global subtotal, sales_tax, total, pizza_price, pizza_cost

    pizza_size = input("Enter the size of the pizza (S, M, L, or XL): ")
    
    if pizza_size == "S":
        pizza_price = PR_SMALL
    elif pizza_size == "M":
        pizza_price = PR_MEDIUM
    elif pizza_size == "L":
        pizza_price = PR_LARGE
    elif pizza_size == "XL":
        pizza_price = PR_XLARGE
    else:
        print("Invalid pizza size entered. Using the default small pizza size.")
        pizza_price = PR_SMALL

    pizza_cost = num_pizza * pizza_price
    breadsticks_cost = num_breadsticks * PR_BREADSTICKS
    drinks_cost = num_drinks * PR_DRINK

    subtotal = pizza_cost + breadsticks_cost + drinks_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    money_format = '{:,.2f}'
    print('------------------------------')
    print('**** Palermos Pizza ****')
    print('The Best Pizza Parlor In The West')
    print('------------------------------')
    print('Pizza Cost:                                   $  ' + money_format.format(pizza_cost))
    print('Beverage cost:                                $  ' + money_format.format(num_drinks * PR_DRINK))
    print('Breadsticks Cost:                             $  ' + money_format.format(num_breadsticks * PR_BREADSTICKS))
    print('Subtotal:                                     $  ' + money_format.format(subtotal))
    print('Sales Tax:                                    $  ' + money_format.format(sales_tax))
    print('Total:                                        $  ' + money_format.format(total))
    print('------------------------------')
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()--')
    print('Pizzas Ordered:                                 ' + money_format.format(num_pizza))
    print('Drinks Ordered:                                 ' + money_format.format(num_drinks))
    print('Breadsticks Ordered:                            ' + money_format.format(num_breadsticks))
    print('Subtotal:                                     $ ' + money_format.format(subtotal))
    print('Sales Tax:                                    $ ' + money_format.format(sales_tax))
    print('Total:                                        $ ' + money_format.format(total))
    print('------------------------------')
    print(datetime.datetime.now())


if __name__ == "__main__":
    main()
