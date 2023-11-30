#Name: Christopher Miller
#Program Purpose: Payroll report. Calculating pay. Fresh Foods.

import datetime

# LISTS OF DATA #
employees = [
    "Smith, James       ",
    "Johnson, Patricia  ",
    "Williams, John     ",
    "Brown, Micheal     ",
    "Jones, Elizabeth   ",
    "Garcia, Brian      ",
    "Miller, Deborah    ",
    "Davis, Timothy     ",
    "Rodriguez, Ronald  ",
    "Martinez, David    ",
    "Hernandez, Lisa    ",
    "Lopez, Nancy       ",
    "Gonzales, Betty    ",
    "Wilson, Sandra     ",
    "Anderson, Margie   ",
    "Thomas, Daniel     ",
    "Taylor, Steven     ",
    "Moore, Andrew      ",
    "Jackson, Donna     ",
    "Martin, Yolanda    ",
    "Lee, Carolina      ",
    "Perez, Kevin       ",
    "Thompson, Brian    ",
    "White, Deborah     ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S", "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M", ]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38, 28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_employees = len(employees)

# NEW LISTS FOR CALCULATED AMOUNTS #

gross_pay = []
federal_tax = []
state_tax = []
social_security = []
medicare = []
retirement = []
net_pay = []

total_gross = 0
total_net = 0

# TUPLES OF CONSTANTS #
#           C       S       J       M
# indexes   0       1       2       3
PAY_RATE = (16.5,   15.75,  15.75,  19.5)

#           fed     state   ss      med     ret
# indexes   0       1       2       3       4
DED_RATE = (.12,    .03,    .062,   .0145,  .04 )

# DEFINE PROGRAM FUNCTIONS #
def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    job_type = input("Enter job type (C/S/J/M): ")
    hours_worked = int(input("Enter hours worked: "))

def perform_calculations():
    global total_gross, total_net

    for i in range(num_employees):

    #calculate gross pay#
        if job[i] == "C":
            pay = hours[i] *PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]
    
    #calculate deductions#
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        ss = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]

        

    # STUDENTS (ME) DEDUCTIONS HERE #

        net = pay - fed - state - ss - med - ret #other deducions go here

    #add to totals
        total_gross += pay
        total_net += net

    #append amounts to lists
        gross_pay.append(pay)
        federal_tax.append(fed)
        state_tax.append(state)
        social_security.append(ss)
        medicare.append(med)
        retirement.append(ret)
        net_pay.append(net)
    #STUDENTS: append other deductions and net pay here:

def display_results():
    currency = '8,.2f'
    line= '-------------------------------------------------------'
    tab = "\t"

    print(line)
    print('******************FRESH FOODS MARKET******************')
    print('-----------------WEEKLY PAYROLL REPORT-----------------')
    print(tab + str(datetime.datetime.now()))
    print(line)
    titles1 = "Employee Name" + tab + "       " + "Code" + tab + "Gross" + tab
    titles2 = "    " + "Federal Income Tax" + tab + "   " + "State Income Tax" + tab + "Social Security" + tab + "  " + "Medicare" + tab + "Net"
    print(titles1 + titles2)
 #STUDENT CREATE MISSING CODE TO PRINT EMPLOYEE DATA ONE LINE AT A TIME
    for i in range(num_employees):
        data1 = employees[i] + "    " + job[i] + "      " + format(gross_pay[i], currency) + "   " + format(federal_tax[i], currency) + "               " + format(state_tax[i], currency)
        data2 = "             " + format(social_security[i], currency) + "          " + format(medicare[i], currency) + "       " + format(net_pay[i], currency)
        print(data1 + data2)
    print(line)
    print("********************** TOTAL GROSS: $" + format(total_gross, currency))
    print("********************** TOTAL NET  : $" + format(total_net, currency))

#main program execution#
main( )