# NAME : Christopher Miller
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
# ------------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (prise per chew: one chew per month)
#   Small dogs, Up to 25 lbs: $0.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99


import datetime

# Define global variables
dog_vax_arr = ["Bortadella", "DAPP", "Influenza", "Leptospirosis",
               "Influenza", "Lyme Disease", "Rabies", "Full Vaccine Package", "NONE"]
cat_vax_arr = ["Leukemia", "Viral Rhinotracheitis",
               "Rabies", "Full Vaccine Package"]

PRICES = {
    "Bortadella": 30,
    "DAPP": 35,
    "Influenza": 48,
    "Leptospirosis": 21,
    "Lyme Disease": 41,
    "Rabies": 25,
    "Full Vaccine Package": 0,
    "Leukemia": 35,
    "Viral Rhinotracheitis": 30,
    "Feline Rabies": 0,
}

PR_CHEWS = {
    "Small dogs (Up to 25 lbs)": 9.99,
    "Medium-sized dogs (26 to 50 lbs)": 11.99,
    "Large dogs (51 to 100 lbs)": 13.99,
    "Cats": 8.00,
}


def main():
    more = True
    while more:
        pet_name, pet_type, pet_weight = get_user_data()
        if pet_type.upper() == "D":
            pet_vax_type, num_chews = get_dog_data(pet_name)
            vax_cost, chews_cost, total = perform_dog_calculations(
                pet_vax_type, pet_weight, num_chews)
            display_pet_results(
                pet_name, dog_vax_arr[pet_vax_type-1], vax_cost, chews_cost, total)
        else:
            pet_vax_type, num_chews = get_cat_data(pet_name)
            vax_cost, chews_cost, total = perform_cat_calculations(
                pet_vax_type, num_chews)
            display_pet_results(
                pet_name, cat_vax_arr[pet_vax_type-1], vax_cost, chews_cost, total)
        ask_again = input(
            "\nWould you like to process another pet (Y or N)?: ")
        if ask_again.upper() == "N" or ask_again.upper() == "NO":
            more = False
    print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')


def get_user_data():
    pet_name = input('Pet name: ')
    pet_type = input('Is this a pet dog (D) or cat (C)? ')
    pet_weight = int(input('Weight of your pet (in pounds): '))
    return pet_name, pet_type, pet_weight


def get_dog_data(pet_name):
    print("\n Dog Vaccines:")
    for i, vaccine in enumerate(dog_vax_arr):
        print(f"{i + 1}. {vaccine}")
    pet_vax_type = int(input("Enter the vaccine number: "))
    print("\nMonthly heartworm prevention medication is recommended for all dogs.\n")
    heart_yesno = input(
        f"Would you like to order monthly heartworm medication for {pet_name} (Y/N)? ")
    num_chews = int(input("How many heartworm chews would you like to order? ")
                    ) if heart_yesno.upper() == "Y" else 0
    return pet_vax_type, num_chews


def perform_dog_calculations(pet_vax_type, pet_weight, num_chews):
    vax_cost = PRICES[dog_vax_arr[pet_vax_type-1]]
    if pet_vax_type == 8:
        vax_cost = 0.85 * sum(PRICES.values())
    chews_cost = 0
    if num_chews != 0:
        if pet_weight <= 25:
            chews_cost = num_chews * PR_CHEWS["Small dogs (Up to 25 lbs)"]
        elif 25 < pet_weight <= 50:
            chews_cost = num_chews * \
                PR_CHEWS["Medium-sized dogs (26 to 50 lbs)"]
        else:
            chews_cost = num_chews * PR_CHEWS["Large dogs (51 to 100 lbs)"]
    total = vax_cost + chews_cost
    return vax_cost, chews_cost, total


def get_cat_data(pet_name):
    print("\n Cat Vaccines:")
    for i, vaccine in enumerate(cat_vax_arr):
        print(f"{i + 1}. {vaccine}")
    pet_vax_type = int(input("Enter the vaccine number: "))
    print("\nMonthly heartworm prevention medication is recommended for all cats.\n")
    heart_yesno = input(
        f"Would you like to order monthly heartworm medication for {pet_name} (Y/N)? ")
    num_chews = int(input("How many heartworm chews would you like to order? ")
                    ) if heart_yesno.upper() == "Y" else 0
    return pet_vax_type, num_chews


def perform_cat_calculations(pet_vax_type, num_chews):
    vax_cost = PRICES[cat_vax_arr[pet_vax_type-1]]
    if pet_vax_type == 4:
        vax_cost = 0.85 * sum(PRICES.values())
    chews_cost = num_chews * PR_CHEWS["Cats"] if num_chews != 0 else 0
    total = vax_cost + chews_cost
    return vax_cost, chews_cost, total


def display_pet_results(pet_name, vax_type, vax_cost, chews_cost, total):
    line = '-----------------------------------------'
    moneyf = '>10,.2f'
    print(line)
    print(' PET VACCINES AND MEDICATION ')
    print(line)
    print(f'Pet Name:              {pet_name}')
    print(f'Vaccine Received:      {vax_type}')
    print(f'Vaccine Cost:         ${vax_cost:{moneyf}}')
    print(f'Heartworm Chews Cost: ${chews_cost:{moneyf}}')
    print(f'Total Cost:           ${total:{moneyf}}')


if __name__ == "__main__":
    main()
