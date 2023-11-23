#Name: Felix Barrientos
#Program Purpose: This program uses llists to find personal preperty tax for a vehicle in Charlottesville
#   and produces a report which displays all data and the total tax due

#Personal Property Tax in Charlottesville:
#   -$4.20 per $100 of vehicle value (4.2% per year)
#   -$Paid every six months
# Personal Property Tax Relief (PPTR):
# Eligibility: Owned or leased vehicles which are predominarely used for non-business
#   purposes and have passenger licence plates
#   -Tax relief for qualified vehicles is 33%

import datetime

#DEFINE TAX RATES#
Personal_Property_Tax = .042
Relief_Rate = .33

#create list data#
vehicle = ["2019 Volvo",
           "2018 Toyota",
           "2022 Kia",
           "2020 Ford",
           "2023 Honda",
           "2019 Lexus",]
vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["Y", "Y", "Y", "Y", "Y", "Y",]

owner_name = ["Brand, Brenda    ",
              "Smith, Carter    ",
              "Johnson, Bradley ",
              "Garcia, Jennifer ",
              "Henderson, Leticia",
              "White, Danielle  ",]
ppt_owed = []

num_vehicles = len(vehicle)
tax_due = 0
total = 0

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total

    for i in range(num_vehicles):
    
        tax_due = (vehicle_value[i] * Personal_Property_Tax) / 2
        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * .67

        ppt_owed.append(tax_due)

        total = total + tax_due
    
def display_results():
    moneyf = '8,.2f'
    line=("-----------------------------------------------------------------")
    tab = "\t"

    print(line)
    print("*******************PERSONAL PROPERTY TAX REPORT******************")
    print("                     Charlottesville, Virginia")

    print("\n\t\tRUN DATE/TIME: " +str(datetime.datetime.now()))
    print("\nNAME" + tab + tab +  tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + " TAX DUE")

    for i in range(num_vehicles):
        dataline1 = owner_name[i] + tab + vehicle[i] + tab + format(vehicle_value[i],moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + format(ppt_owed[i],moneyf)
        print(dataline1 + dataline2)

    print(line)
    print("******************************************** TOTAL TAX DUE: " + tab + format(total,moneyf))

main()